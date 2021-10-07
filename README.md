# Self Organising Map for Clustering of Atomistic Samples - V2
## Description
Self Organising Map (also known as Kohonen Network) implemented in Python for clustering of atomistic samples through unsupervised learning. The program allows the user to select wich per-atom quantities to use for training and application of the network, this quantities must be specified in the LAMMPS input file that is being analysed. The algorithm also requires the user to introduce some of the networks parameters:
- _f_: Fraction of the input data to be used when training the network, must be between 0 and 1.
- SIGMA: Maximum value of the _sigma_ function, present in the neighbourhood function.
- ETA: Maximum value of the _eta_ funtion, which acts as the learning rate of the network.
- N: Number of output neurons of the SOM, this is the number of groups the algorithm will use when classifying the atoms in the sample.

The input file must be inside the same folder as the main.py file. Furthermore, the input file passed to the algorithm must have the LAMMPS dump format, or at least have a line with the following format:

`ITEM: ATOMS id x y z feature_1 feature_2 ...`

To run the software, simply execute the following command in a terminal (from the folder that contains the files and with a python environment activated):

`python3 main.py`

Check the software report in the general repository for more information: https://github.com/rambo1309/SOM_for_Atomistic_Samples_GeneralRepo

## Dependencies:
This software is written in Python 3.8.8 and uses the following external libraries:
- NumPy 1.20.1
- Pandas 1.2.4

(Both packages come with the basic installation of Anaconda)

## What's new in V2:
Its important to clarify that V2 of the software isn't designed to replace V1, but to be used when multiple files need to be analysed sequentially with a network that has been trained using a specific training file. It is recommended for the user to first use V1 to explore the results given by different parameters and features of the sample, and then to use V2 to get consistent results for a series of samples. Another reason why V1 will be continually updated is its command-line interactive interface, which allows the users to implement the algorithm without ever having to open and edit a python file.

The most fundamental change with respect to V.1 is the way of communicating with the program. While V.1 uses an interactive command-line interface, V.2 requests an input_params.py file that contains a dictionary specifying the parameters and sample files for the algorithm.

Check the report file in the repository for a complete description of the changes made in the software.

## Updates:
Currently working on giving the user the option to change the learning rate funtion, eta, with a few alternatives such as a power-law and an exponential decrease.
Another important issue still to be addressed is the writing times of the output files. 
