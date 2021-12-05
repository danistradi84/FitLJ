"""Test for the ase_database.py module"""

from fitlj.io.ase_database import AtomicSimulationEnvironmentDataBase


def test_get_energies():
    """test for get_energies function"""

    database = AtomicSimulationEnvironmentDataBase(database_filename='files/bulk_copper_molecular_dynamics_1000K.db')

    reference_energies = [47.87802707696225,
                          48.123704052434604,
                          48.80413381282413,
                          49.85762977482733,
                          51.1838561325066,
                          52.61358194135562,
                          53.92876689839439,
                          54.93992468460648,
                          55.4934606196465,
                          55.580404135034826,
                          55.32437874286174]

    assert database.get_energies() == reference_energies
