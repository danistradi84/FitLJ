import numpy
from ase.calculators.lj import LennardJones
from scipy.optimize import fmin


class FitModel:
    """Fit a Lennard-Jones model using a series of configurations

    Args:
        database (str) = name of the database

        lennard_jones_parameters (float) = initial guess for Lennard Lones parameters [epsilon, sigma]

    Example:

        this class can be called using
        >>> from fitlj.fitting.fit_model import FitModel
        >>> FitModel(database=database, lennard_jones_parameters=[0.01,3.0])

    """

    def __init__(self, database=None, lennard_jones_parameters=None):
        self.database = database
        self.lennard_jones_parameters = lennard_jones_parameters

    def lennard_jones_model(self, lennard_jones_parameters):
        """Predict energies using a Lennard Jones model"""

        # Get database
        database = self.database

        # Get Lennard-Jones parameters epsilon and sigma
        epsilon, sigma = lennard_jones_parameters

        # Define Lennard-Jones calculator
        lennard_jones_calculator = LennardJones(sigma=sigma, epsilon=epsilon)

        # Get atoms from database
        all_atoms = [row.toatoms() for row in database.select()]

        # Set Lennard-Jones calculator for each atoms
        [atoms.set_calculator(lennard_jones_calculator) for atoms in all_atoms]

        # Predict energies based on the Lennard-Jones parameters
        predicted_energies = numpy.array([atoms.get_potential_energy() for atoms in all_atoms])
        return predicted_energies

    def objective_function(self, lennard_jones_parameters):
        """Objective function to optimize Lennard Jones Parameters"""

        # Get database
        database = self.database

        # Get Lennard-Jones model
        lennard_jones_model = self.lennard_jones_model

        # Get ground truth energies
        ground_truth_energies = numpy.array([row.energy for row in database.select()])

        # Calculate error
        error = ground_truth_energies - lennard_jones_model(lennard_jones_parameters)

        # Calculate mean squared error
        mean_squared_error = numpy.mean(error**2)

        return mean_squared_error

    def fit_lennard_jones_model(self):
        """Fit a Lennard-Jones model"""

        # Get objective function
        objective_function = self.objective_function

        # Get initial Lennard-Jones parameters
        lennard_jones_parameters = self.lennard_jones_parameters

        # Fit Lennard-Jones parameters
        fitted_lennard_jones_parameters = fmin(objective_function, lennard_jones_parameters)

        return fitted_lennard_jones_parameters
