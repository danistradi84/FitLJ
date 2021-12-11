from fitlj.fit_model import FitModel
from fitlj.io import AtomicSimulationEnvironmentDataBase

# Load the database file 
database = AtomicSimulationEnvironmentDataBase(database_filename='Cu.db')

# Connect to the database 
database = database.connect_to_database()

# Initial guess for sigma
sigma_initial_guess = 15.0

# Initial guess for epsilon 
epsilon_initial_guess = 3.5 

# Fit a Lennard Jones model to the configurations present in the database
model = FitModel(database=database, 
                 lennard_jones_parameters=[sigma_initial_guess, epsilon_initial_guess])
sigma, epsilon = model.fit_lennard_jones_model()

# Print the fitted values
print(f'The fitted value of sigma is: {sigma:.5f} eV.')
print(f'The fitted value of epsilon is: {epsilon:.5f} Ang.')
