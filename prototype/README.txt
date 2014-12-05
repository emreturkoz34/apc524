Usage for the Python user i/o and wrapper:

Command: ./chemtable_io.py
Input:	"chemtable_inputs" text file. 
	This file must be in the same directory as "chemtable_io.py". 
	The directory must also contain any data files referenced in the 
	input file, for example "CH4_P01_0chi00001tf0300to0300.kg
Output: CvsT.pdf, a plot of the best progress variable  vs. temperature
	Printouts indicating details of the best progress variable

Files:	chemtable_io.py
	findprogvar.py
	iofuncs.py
	combinations.py

Functionality:

	NOTE: the Python wrapper has not yet been connected to the C++
	functions being developed in parallel. Where these functions
	would be called, instead there are placeholders or dummy functions.
	However, the key Python functionality has been implemented.

chemtable_io.py: The main user interface functions that parses the inputs
		file and calls other functions to process the data
findprogvar.py:	Contains a Python function which performs the calculations 		required for the first part of the program (determining the 		best progress variable). This function also has placeholders
		instead of calls to C++ functions.
iofuncs.py:	Contains Python functions and classes called by the other
		files for processing data.
combinations.py: Contains a function that generates a matrix that can be 
		used to calculate all possible combinations of elements in a
		vector.	

		