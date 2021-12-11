import numpy
from ase.calculators.emt import EMT
from ase.lattice.cubic import SimpleCubic, FaceCenteredCubic, BodyCenteredCubic
from ase.db import connect

# Define list of lattice constant values
lattice_constants = numpy.linspace(2.0, 6.0, 10)

# Connect to the database
database = connect('Cu.db')

# Loop over the crystalline lattice systems
for lattice in [SimpleCubic, FaceCenteredCubic, BodyCenteredCubic]:

    # Loop over the lattice constant values
    for a in lattice_constants:

        # Create the crystal unit cell
        atoms = lattice('Cu', latticeconstant=a)

        # Attach a calculator
        atoms.calc = EMT()

        # Get the potential energy
        energy = atoms.get_potential_energy()

        # Write the structure to the database
        database.write(atoms)
