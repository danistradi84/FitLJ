"""Test for the ase_database.py module"""
from fitlj.io import AtomicSimulationEnvironmentDataBase


def test_get_energies():
    """test for get_energies function"""

    database = AtomicSimulationEnvironmentDataBase(database_filename='files/bulk_copper_molecular_dynamics_1000K.db')

    reference_energies = [47.87802708, 48.07638877, 48.6523761, 49.56921409, 50.74681078,
                          52.06426054, 53.38301906, 54.5185143, 55.32767403, 55.75613736,
                          55.83521654]

    output_energies = database.get_energies()

    assert len(output_energies) == len(reference_energies)
    assert all(abs(a - b) < 1e-6 for a, b in zip(output_energies, reference_energies))
