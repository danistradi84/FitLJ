Fitting a Lennard-Jones potential for bulk Cu 
=============================================

In this tutorial you will learn how to create a dataset of structures, calculate their energies, and use the FitLJ package to fit a Lennard-Jones potential.

Creating the database
*********************

A necessary requirements for fitting an interatomic potential is to have a database of structures representative of the possible atomic configurations of the material of interest. The energies of these configurations are used as ground truth for the fitting procedure. 

Here, we will use ASE to create a data set of different bulk structures of Cu at different volumes. To make the potenital as general and transferable as possible among different configuratiosn, we will consider three different crystalline systems: 

* Simple cubic:

  .. image:: simple_cubic.png

* Face-centered cubic:

  .. image:: face_centered_cubic.png

* Body-centerd cubic:

  .. image:: body_centered_cubic.png

The volume of the three crystalline structures is defined by the lattice constant *a*. The ground truth energies will be calculated using the Effective Medium Theory. 

.. warning::

   The Effective Medium Theory used in this tutorial is not intended to produce accurate results and it is intended only for pedagogical purposes. For production simulations, one might want to use a more accurate and computationally intensive electronic structure method such as `Density Functional Theory <https://en.wikipedia.org/wiki/Density_functional_theory>`_.

The script `run_emt <run_emt.py>`_ uses ASE to loop over different values of the lattice constant *a* for the three different crystalline structures. The calculated structures and associated energies are then dumped into a database. The latter will be used later for the fitting procedure.

.. literalinclude:: run_emt.py
   :language: python
   :linenos:

Fitting the Lennard-Jones potential 
***********************************

Once the database has been created, the FitLJ program can be used to read the database and use it to fit the Lennard Jones potential parameters :math:`\sigma` and :math:`\epsilon`.

The script `fit <fit.py>`_ load the database ``Cu.db`` previously created and fit the parameters of a Lennard Jones potenital to the energies of the structures contained in the database.

.. literalinclude:: fit.py
   :language: python 
   :linenos:

The optimized values of :math:`\sigma` and :math:`\epsilon` are printed after the optimization has successfully terminated:

.. code-block:: bash
   :linenos:

   >>>python3 fit.py 
   Optimization terminated successfully.
            Current function value: 730.106876
            Iterations: 22
            Function evaluations: 72
   The fitted value of sigma is: 19.05469 eV.
   The fitted value of epsilon is: -0.50313 Ang.

.. warning::
   
   In order for the optimization procedure to be succesfull, reasonable starting guesses for the :math:`\sigma` and :math:`\epsilon` parameters must be chosen. If the starting guesses are very far from the final, optimized values, the fitting procedure might not be successful. 
   