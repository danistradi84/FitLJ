Installation
============

Dependencies
------------
FitLJ requires the Atomic Simulation Environment (`ASE <https://wiki.fysik.dtu.dk/ase/>`_) as well as the `ASAP <https://wiki.fysik.dtu.dk/asap>`_ codes to be installed on your local Linux installation. We reccoment to install these packages either in a dedicated ``conda`` environment or via ``pip3``. 

Anaconda
********

.. code-block:: bash 
   :linenos:

   >>> conda -c install conda-forge ase
   >>> conda -c install conda-forge asap

Pip3
****

.. code-block:: bash 
   :linenos:

   >>> pip install ase 
   >>> pip install asap

Environment variables
---------------------

Once the dependencies have been installed, the next step is to export the path where the FitLJ program is located. This can be done by adding the following line in your ``.bashrc`` file,

.. code-block:: bash 
   :linenos:

   PYTHONPATH="$HOME/home/<user>/<path-to-folder>/fitlj:$PYTHONPATH"

where ``<user>`` and ``<path-to-folder>`` are your username and the path to the folder of the FitLJ program.