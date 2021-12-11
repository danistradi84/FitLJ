import numpy
from ase.db import connect


class AtomicSimulationEnvironmentDataBase:
    """Read a database created using ASE

    Args:
        database_filename (str): name of the ASE database.

    Returns:
        str: SQLite3 database

    Example:

    >>> # Read an ASE database
    >>> from fit.io.database import AtomicSimulationEnvironmentDataBase
    >>> database = AtomicSimulationEnvironmentDataBase(database_filename='database.db')

    """

    def __init__(self, database_filename=None):
        self.database_filename = database_filename

    def connect_to_database(self):
        """Connect to the ASE database"""

        # Connect to database
        database = connect(self.database_filename)
        return database

    def get_energies(self):
        """Connect to ASE database and get array with total energies"""

        # Connect to database
        database = self.connect_to_database()

        # Get ground truth energies from atoms
        ground_truth_energies = numpy.array([row.energy for row in database.select()])
        return ground_truth_energies
