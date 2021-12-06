from fitlj.fitting.fit_model import FitModel
from fitlj.io.ase_database import AtomicSimulationEnvironmentDataBase

database = AtomicSimulationEnvironmentDataBase(database_filename='bulk_copper_molecular_dynamics_1000K.db')
database = database.connect_to_database()
model = FitModel(database=database, lennard_jones_parameters=[0.4, 2.5])
fit = model.fit_lennard_jones_model()
print(fit)
