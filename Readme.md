===============================
Orders and Dependencies
===============================

This program takes two text files, an orders.txt with a list of
order numbers in a store, and dependencies.txt, which shows  
how some orders are connected to/rely on other orders.
These connections between orders are currently presented poorly.
This program aims to make it easier to understand how these orders
are connected.


Quickstart
----------

The main dependencies in this programming is between modules, 
therefore setup is simple.

The only library to install is the pandas library, which is 
done by the following command:

	pip install pandas

It should be noted that the input_url and output_url in the 
hlepr.py files should be changed to the appropriate path.
 
To run the program, type in the following command:
	python main.py 
	

Running Tests
-------------

Manual/Exploratory testing:

The following is a list of manual tests that can be done to check
if the program is running as it should.

	1) Add a dependencies.txt file with 1 order / dependency pair
		Print what is being read in (the dataframe).
	2) Add a dependencies.txt file with 2 orders / depend pair 
		of different orders.
		Print what is being read in (the dataframe).
	3) Add a dependencies.txt file with 2 orders / depend pair 
		of the same order.
		Print what is being read in (the dataframe).
	4) Add a dependencies.txt file with 3+ orders / depend pairs,  
		having at least 1 of the same order and 1 different.
		Print what is being read in (the dataframe).
	6) Is the itertuples() function in main.py breaking down 
		each line's id and dependency correctly.
	7) Is the output.txt file being created.
	8) Is the output.txt file displaying the right content 
		Repeat this for Tests 1 to 4 scenarios.
	9) Is the output.txt file displying the content in the right
		layout. 
		Repeat this for Tests 1 to 4 scenarios.

Unit tests:

	*Use unittest as test runner.
	
	Many of the Manual tests can be further broken down to unit tests.
	Others can be added.
	The cleanest existing example is #6 (out of time so will breakdown:)
		Expected output would be (1,2) for first line.
		Assert it, see if there is an error.


Integrated tests:

	*Use unittest as test runner.

	Many of the Manual tests can be integrated tests. 
	Others can be added.
	The cleanest existing example are Manual tests 6 and 7.