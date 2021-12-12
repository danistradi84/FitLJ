## Description 

FitLJ is a program to fit a Lennard Jones potential using a database of atomic structures calculated using the Atomic Simulation Environment.

## Installation

To install fitlj from GitHub repository, do:

```console
git clone https://github.com/danistradi84/fitlj.git
cd fitlj
python3 -m pip install .
```

## Dependencies 

The following packages must be installed in order to run FitLJ: 

* Python (>=3.8)
* Numpy
* Scipy 
* Atomic Simulation Environment 
* Sphinx 
* Sphinx-autoapi

## How to use fitlj

```console
from fitlj.fit_model import FitModel
from fitlj.io import AtomicSimulationEnvironmentDataBase

database = AtomicSimulationEnvironmentDataBase(database_filename='Cu.db')

database = database.connect_to_database()

sigma_initial_guess = 15.0
epsilon_initial_guess = 3.5

model = FitModel(database=database, lennard_jones_parameters=[sigma_initial_guess, epsilon_initial_guess])
sigma, epsilon = model.fit_lennard_jones_model()
```

## Documentation

Full documentation is aviailable at https://fitlj.readthedocs.io/en/latest/ 

## Contributing

If you want to contribute to the development of fitlj,
have a look at the [contribution guidelines](CONTRIBUTING.md).

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [NLeSC/python-template](https://github.com/NLeSC/python-template).
