from fitlj.fit_model import FitModel
from fitlj.io import AtomicSimulationEnvironmentDataBase

database = AtomicSimulationEnvironmentDataBase(database_filename='argon.db')
database = database.connect_to_database()
model = FitModel(database=database, lennard_jones_parameters=[0.01, 3.5])
fit = model.fit_lennard_jones_model()
print(fit)
