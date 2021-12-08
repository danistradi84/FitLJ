"""Test for the ase_database.py module"""

from fitlj.io.ase_database import AtomicSimulationEnvironmentDataBase
from fitlj.fitting.fit_model import FitModel


def test_fit_lennard_jones_model():
    """test for get_energies function"""

    database = AtomicSimulationEnvironmentDataBase(database_filename='argon.db')

    database = database.connect_to_database()
    model = FitModel(database=database, lennard_jones_parameters=[0.01, 3.5])
    fit = model.fit_lennard_jones_model()

    reference_fit = [0.00592987, 3.73316583]
    assert all(abs(a-b) < 1e-4 for a, b in zip(fit, reference_fit))
