# Import classes from ASE
from ase.db import connect


class AtomicSimulationEnvironmentDataBase:
    """Read a database created using ASE


    Parameters:


    database_filename: str
       name of the ASE database (example: 'database.db')
    """

    def __init__(self, database_filename=None):
        self.database_filename = database_filename

    def get_energies(self):
        """Connect to database and get array with total energies"""

        # Connect to database
        database = connect(self.database_filename)

        # Get energies from atoms
        atoms = [database.get_atoms(selection=i+1) for i in range(len(database))]

        # Get energies from atoms
        energies = [i.get_potential_energy() for i in atoms]
        return energies
