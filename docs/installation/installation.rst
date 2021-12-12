Installation
============

Required dependencies
---------------------

* `python <https://www.python.org/>`_ 
* `numpy <https://numpy.org/>`_ 
* `scipy <https://scipy.org/>`_ 
* `ase <https://wiki.fysik.dtu.dk/ase/>`_ 
* `sphinx <https://www.sphinx-doc.org/en/master/>`_
* `sphinx autoapi <https://sphinx-autoapi.readthedocs.io/en/latest/>`_

Installing dependencies
-----------------------
The required dependencies can be installed either in a dedicated `Anaconda <https://www.anaconda.com/>`_ environment or in a dedicated `Python virtual environment <https://virtualenv.pypa.io/en/latest/#>`_  via ``pip``. 

Installing dependencies using conda (Anaconda)
**********************************************

First, create a new conda environment and activate it:

.. code-block:: bash 
   :linenos:

   >>> conda create --name fitlj python=3.8 
   >>> conda activate fitlj 

Then, install the required packages:

.. code-block:: bash 
   :linenos:

   >>> conda -c install conda-forge numpy scipy ase sphinx sphinx-autoapi

Installing dependencies using pip
*********************************

First, create a new environment and activate it:

.. code-block:: bash 
   :linenos:

   >>> python3 -m venv <path-to-virtual-environment> 
   >>> source <path-to-virtual-environment>/bin/activate

Then install the required packages:

.. code-block:: bash 
   :linenos:

   >>> pip install numpy 
   >>> pip install scipy 
   >>> pip install ase
   >>> pip install sphinx  
   >>> pip install sphinx-autoapi

Environment variables
---------------------

The following environment variable should be added to your PYTHONPATH

.. code-block:: bash 
   :linenos:

   cd <path-to-folder>; export PYTHONPATH=$(pwd):$PYTHONPATH

where ``<path-to-folder>`` is the path to the folder of the FitLJ program.
