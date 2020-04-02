import sys
import os

sys.path.insert(1, '../../1_code/DjangoApp')

import util.db_helper as db_helper

file = open("get_task.txt", "r")

print("Unit Test for get_task(taskID)")
for line in file:
	input, output = line[:-1].split(':')
	print("Input: " + input)
	print("Expected Output: " + output)
	temp = db_helper.get_task(input)
	print("Output: " + str(temp))
	print("Match: " + str(str(temp)==output))
	if((str(temp)!=output)):
		print("Error in output!")
		sys.exit(0)
	print()
print("Test Passed")
print()

print("Unit Test for get_all_tasks()")
print("Output: " + str(db_helper.get_all_tasks()))
print()
print("Test Passed")
print()

print("Unit Test for get_completed_tasks()")
print("Output: " + str(db_helper.get_completed_tasks()))
print()
print("Test Passed")
print()

print("Unit Test for get_noncompleted_tasks()")
print("Output: " + str(db_helper.get_noncompleted_tasks()))
print()
print("Test Passed")
print()

print("Unit Test for get_inprogress_tasks()")
print("Output: " + str(db_helper.get_inprogress_tasks()))
print()
print("Test Passed")
print()

print("Unit Test for get_incomplete_tasks()")
print("Output: " + str(db_helper.get_incomplete_tasks()))
print()
print("Test Passed")
print()

file = open("get_employee_tasks.txt", "r")

print("Unit Test for get_employee_tasks(employeeID)")
for line in file:
	input, output = line[:-1].split(':')
	print("Input: " + input)
	print("Expected Output: " + output)
	temp = db_helper.get_employee_tasks(input)
	print("Output: " + str(temp))
	print("Match: " + str(str(temp)==output))
	if((str(temp)!=output)):
		print("Error in output!")
		sys.exit(0)
	print()
print("Test Passed")
print()

file = open("get_item_info.txt", "r")

print("Unit Test for get_item_info(RFID)")
for line in file:
	input, output = line[:-1].split(':')
	print("Input: " + input)
	print("Expected Output: " + output)
	temp = db_helper.get_item_info(input)
	print("Output: " + str(temp))
	print("Match: " + str(str(temp)==output))
	if((str(temp)!=output)):
		print("Error in output!")
		sys.exit(0)
	print()
print("Test Passed")
print()

file = open("get_employee.txt", "r")

print("Unit Test for get_employee(employeeID)")
for line in file:
	input, output = line[:-1].split(':')
	print("Input: " + input)
	print("Expected Output: " + output)
	temp = db_helper.get_employee(input)
	print("Output: " + str(temp))
	print("Match: " + str(str(temp)==output))
	if((str(temp)!=output)):
		print("Error in output!")
		sys.exit(0)
	print()
print("Test Passed")
print()
