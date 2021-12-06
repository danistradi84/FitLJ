# Example based on https://wiki.fysik.dtu.dk/ase/tutorials/md/md.html

# Import classes from ASE
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.langevin import Langevin
from ase.io.trajectory import Trajectory
from ase.db import connect
from ase import units

# Import EMT class from ASAP3
from asap3 import EMT

# User-defined parameters
supercell_size = [5, 5, 5]  # Supercell size
temperature = 1000  # Temperature [K]
number_of_steps = 5000  # Total number of MD steps
step_interval = 50  # Step interval to print the MD snapshot
timestep = 0.5  # Timestep of the MD simulation
output_filename = 'bulk_copper_molecular_dynamics'  # Global name of the output files

# Set up an FCC crystal
atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                          symbol="Cu",
                          size=supercell_size,
                          pbc=False
                          )

# Set Effective Medium Theory calculator
atoms.calc = EMT()

# Set the momenta corresponding to a temperature T = 1000 K
MaxwellBoltzmannDistribution(atoms=atoms,
                             temperature_K=temperature
                             )

# Run MD at T = 1000 K the Langevin algorithm,
# a time step of 5 fs and a friction coefficient to 0.02 atomic units.
dyn = Langevin(atoms=atoms,
               timestep=timestep * units.fs,
               temperature_K=temperature,
               friction=0.002
               )

# Print potential and kinetic energy in the standard output


def printenergy(a=atoms):
    epot = a.get_potential_energy() / len(a)   # Potential energy
    ekin = a.get_kinetic_energy() / len(a)   # Kinetic energy
    instantaneous_temperature = ekin / (1.5 * units.kB)  # Istantaneous temperature
    total_energy = epot + ekin  # Total energy
    print(f"Energy per atom: Epot = {epot:.3f} eV Ekin = {ekin:.3f} eV (T = {instantaneous_temperature:.2f} K) Etot = {total_energy:.3f} eV")

# Attach funciton and print energy


dyn.attach(printenergy, interval=step_interval)

# Save the positions of all atoms
traj = Trajectory(output_filename+'_'+str(temperature)+'K.traj', 'w', atoms)
dyn.attach(traj.write, interval=step_interval)

# Run the dynamics
printenergy()
dyn.run(number_of_steps)

# Read trajectory file
trajectory = Trajectory(output_filename+'_'+str(temperature)+'K.traj')

# Dump trajectory snapshots in a database
database = connect(output_filename+'_'+str(temperature)+'K.db')
for snapshot in enumerate(trajectory):
    database.write(snapshot[1])
