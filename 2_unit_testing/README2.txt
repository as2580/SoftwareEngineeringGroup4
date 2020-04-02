UNIT TESTING README

Unit Testing for database connection:

Running:
	Navigate to 2_unit_testing/database_testing/
	Run "database_testing.py"
	This will test the functions found in "1_code/DjangoApp/util/db_helper.py"
	Program will exit if it finds an output that doesn't match expected output

Modification:
	You can change the test cases by adding to the appropriate text file.
	Each text file is named after the function it tests e.g. "get_task.txt" tests the get_task() function
	In these files each test case is a new line with the input before the ":" and expected output after
	If a function requires multiple input they can be separated by a ","
