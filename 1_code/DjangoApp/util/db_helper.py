import util.db_util as db_util
import datetime

###########################
# TASKS RELATED FUNCTIONS #
###########################
# input parameter(s): 
#	taskID
#		-an int
#		-represents the task's ID
# return value:
#	task
#		-a tuple containing all information for a given tasks
def get_task(taskID):
	if not isinstance(taskID, str):
		taskID = str(taskID)
	if len(taskID) < 1:
		return []
	q = "SELECT * FROM SE_DB.tasks WHERE taskID = " + taskID + ";"
	c = db_util.db_open()
	task = db_util.db_query(c, q)
	db_util.db_close(c)
	return task

# input parameter(s):
#	taskName
#		-a string
#		-represents the title/name of the task
#	description
#		-a string
#		-represents the description of the tasks
# return value: None
def add_task(taskName, description):
	if not isinstance(taskName, str):
		taskName = str(taskName)
	if not isinstance(description, str):
		description = str(description)
	current_time = str(datetime.datetime.now())
	q = "INSERT INTO SE_DB.tasks(taskName, description, state, timeCreated) VALUES('" + taskName
	q = q + "', '" + description + "'," + "'Incomplete','" + current_time + "');"
	c = db_util.db_open()
	db_util.db_execute(c, q)
	db_util.db_close(c)
	

# input parameter(s):
#   taskID
#		-an int
#		-represents the task ID
#   taskName
#		-a string
#		-contains the task name to which the task's task name should be changed
#   description
#		-a string
#		-contains the description to which the task's description should be changed
#   state
#		-a string
#		-contains the state to which the task's state should be changed
#	employeeID
#		-an int
#		-contains the employee's ID to which the task's employeeID should be changed
#	timeCreated
#		-a datetime
#		-contains the time to which the task's creation time should be changed
#	timeCompleted
#		-a datetime
#		-contains the time to which the task's completion time should be changed
# return value: None
def modify_task(taskID, taskName=None, description=None, state=None, employeeID=None, timeCreated=None, timeCompleted=None):
	if not isinstance(taskID, str):
		taskID = str(taskID)
	if not isinstance(taskName, str):
		taskName = str(taskName)
	if not isinstance(description, str):
		description = str(description)
	if not isinstance(state, str):
		state = str(state)
	if not isinstance(employeeID, str):
		employeeID = str(employeeID)
	q = "UPDATE SE_DB.tasks SET taskName = \"" + taskName + "\""
	q = q + ", description = \"" + description + "\""
	q = q + ", state = \"" + state + "\""
	q = q + ", employeeID = \"" + employeeID + "\""
	q = q + ", timeCreated = \"" + timeCreated + "\""
	q = q + ", timeCompleted = \"" + timeCompleted + "\""
	q = q + " WHERE taskID = " + taskID + ";"
	c = db_util.db_open()
	db_util.db_execute(c, q)
	db_util.db_close(c)	


# input parameter(s): 
#	taskID
#		-an int
#		-represents the task's ID
# return value: None
def remove_task(taskID):
	if not isinstance(taskID, str):
		taskID = str(taskID)
	q = "DELETE FROM SE_DB.tasks WHERE taskID = " + taskID + ";"
	c = db_util.db_open()
	db_util.db_execute(c, q)
	db_util.db_close(c)


# input parameter(s): None
# return value:
#	tasks
#		-a list of lists
#		-contains all tasks
#		-nested list is a tuple containing all information for a given tasks
def get_all_tasks():
    q = "SELECT * FROM SE_DB.taskList;"
    c = db_util.db_open()
    tasks = db_util.db_query(c, q)
    db_util.db_close(c)
    return tasks


# input parameter(s): None
# return value:
#	tasks
#		-a list of lists
#		-contains only tasks that are Complete
#		-nested list is a tuple containing all information for a given tasks
def get_completed_tasks():
    q = "SELECT * FROM SE_DB.taskList WHERE state = \"Complete\";"
    c = db_util.db_open()
    tasks = db_util.db_query(c, q)
    db_util.db_close(c)
    return tasks


# input parameter(s): None
# return value:
#	tasks
#		-a list of lists
#		-contains only tasks that are not Complete
#		-nested list is a tuple containing all information for a given tasks
def get_noncompleted_tasks():
    q = "SELECT * FROM SE_DB.taskList WHERE state != \"Complete\";"
    c = db_util.db_open()
    tasks = db_util.db_query(c, q)
    db_util.db_close(c)
    return tasks


# input parameter(s): None
# return value:
#	tasks
#		-a list of lists
#		-contains only tasks that are In Progress
#		-nested list is a tuple containing all information for a given tasks
def get_inprogress_tasks():
    q = "SELECT * FROM SE_DB.tasks WHERE state = \"In Progress\";"
    c = db_util.db_open()
    tasks = db_util.db_query(c, q)
    db_util.db_close(c)
    return tasks


# input parameter(s): None
# return value:
#	tasks
#		-a list of lists
#		-contains only tasks that are Incomplete
#		-nested list is a tuple containing all information for a given tasks
def get_incomplete_tasks():
    q = "SELECT * FROM SE_DB.tasks WHERE state = \"Incomplete\";"
    c = db_util.db_open()
    tasks = db_util.db_query(c, q)
    db_util.db_close(c)
    return tasks
	

# input parameter(s): 
#	employeeID 
#		-an int
#		-represents the employee's ID
# return value:
#	tasks
#		-a list of lists
#		-contains only tasks that are In Progress that have been claimed by the employee with employeeID
#		-nested list is a tuple containing all information for a given tasks
def get_employee_tasks(employeeID):
	if(not employeeID.isdecimal()):
		return []
	if not isinstance(employeeID, str):
		employeeID = str(employeeID)
	if len(employeeID) < 1:
		return []
	q = "SELECT * FROM SE_DB.tasks WHERE state = \"In Progress\" AND  employeeID = " + employeeID + ";"
	c = db_util.db_open()
	tasks = db_util.db_query(c, q)
	db_util.db_close(c)
	return tasks
	
	
# input parameter(s):
#	taskID
#		-an int
#		-represents the task ID
#	new_state
#		-a string
#		-contains the state to which the task's state should be changed
#	employeeID
#		-an int
#		-contains the employee's ID if the state is being changed to "In Progress"
#		-otherwise, should be None
# return value: None
def update_task_state(taskID, new_state, employeeID):
	if not isinstance(taskID, str):
		taskID = str(taskID)
	if not isinstance(new_state, str):
		new_state = str(new_state)
	if not isinstance(employeeID, str):
		employeeID = str(employeeID)
	q = "UPDATE SE_DB.tasks SET state = \"" + new_state + "\""
	if new_state == "Complete":
		current_time = str(datetime.datetime.now())
		q = q + ", timeCompleted = \'" + current_time + "\'"
	elif new_state == "In Progress":
		q = q + ", employeeID = " + employeeID
	q = q + " WHERE taskID = " + taskID + ";"
	c = db_util.db_open()
	db_util.db_execute(c, q)
	db_util.db_close(c)


# input parameter(s): None
# return value: None
def randomly_assign_tasks():
	q = "UPDATE SE_DB.tasks SET employeeID = (select SE_DB.hours.employeeID FROM SE_DB.hours where SE_DB.hours.checkOut is Null order by RAND() limit 1), state ='In Progress'  WHERE state = 'Incomplete';"
	c = db_util.db_open()
	db_util.db_execute(c, q)
	db_util.db_close(c)


###########################
# ITEMS RELATED FUNCTIONS #
########################### 
# input parameter(s): 
#	RFID
#		-an int
#		-represents the item's RFID
# return value:
#	info
#		-a list of lists
#		-contains the name and price of item with matching RFID
#		-nested list is a tuple containing the name and price for the item
def get_item_info(RFID):
	if not isinstance(RFID, str):
		RFID = str(RFID)
	if(not RFID.isdecimal()):
		return []
	q = "SELECT name, price FROM SE_DB.items WHERE RFID = " + RFID + ";"
	c = db_util.db_open()
	info = db_util.db_query(c, q)
	db_util.db_close(c)
	return info
	
	
# input parameter(s): None
# return value:
#	info
#		-a list of lists
#		-contains the name, brand, and price of all items
#		-nested list is a tuple containing the name, brand, and price for the items
def get_items():
	q = "SELECT name, brand, price FROM SE_DB.items"
	c = db_util.db_open()
	info = db_util.db_query(c, q)
	db_util.db_close(c)
	return info


# input parameter(s): 
#	query
#		-a string
#		-a search query entered to find an item
# return value:
#	info
#		-a list of lists
#		-contains the name, brand, and price of item(s) with names containing the query
#		-nested list is a tuple containing the name, brand, and price for the item(s)
def get_search_result(query):
	q = "SELECT name, brand, price, RFID FROM SE_DB.items WHERE name like \"%" + query +"%\""
	c = db_util.db_open()
	info = db_util.db_query(c, q)
	db_util.db_close(c)
	return info


# input parameter(s): 
#	id
#		-an int
#		-an item's RFID
# return value:
#	info
#		-a string
#		-the location of the item (returns a location in the store if available; returns the Back Room if not in the store but in the back room; returns nothing otherwise)
def get_location(id):
	id = str(id)
	q = "SELECT location FROM SE_DB.stock WHERE itemRFID = " + id +" AND location != 'Back Room';"
	c = db_util.db_open()
	info = db_util.db_query(c, q)
	db_util.db_close(c)
	if(len(info) == 1):
		return info[0][0]
	else:
		q = "SELECT location FROM SE_DB.stock WHERE itemRFID = " + id +" AND location = 'Back Room';"
		c = db_util.db_open()
		info = db_util.db_query(c, q)
		db_util.db_close(c)
		if(len(info) == 1):
			return info[0][0]
		else:
			return ""


###############################
# EMPLOYEES RELATED FUNCTIONS #
############################### 
# input parameter(s):
#	employeeID
#		-an int
#		-represents the employee's ID
# return value:
#	employee
#		-a list
#		-contains the employee's last name at employee[0] and the employee's first name at employee[1]
def get_employee(employeeID):
	if(not employeeID.isdecimal()):
		return []
	if not isinstance(employeeID, str):
		employeeID = str(employeeID)
	q = "SELECT lastName, firstName FROM SE_DB.employees WHERE ID = " + employeeID + ";"
	c = db_util.db_open()
	employee = db_util.db_query(c, q)
	db_util.db_close(c)
	return employee


###############################
#   HOURS RELATED FUNCTIONS   #
############################### 
# input parameter(s): None
# return value:
#	hours
#		-a list of lists
#		-contains the employee ID, the employee name, the day of the worked hours, and the number of hours worked for that day in descending date for all employees
def get_all_employee_hours():
	q = "SELECT employeeID, employeeName, day, hours FROM SE_DB.hoursList ORDER BY day DESC"
	c = db_util.db_open()
	hours = db_util.db_query(c, q)
	db_util.db_close(c)
	return hours

# input parameter(s):
#	employeeID
#		-an int
#		-represents the employee's ID
# return value:
#	hours
#		-a list of lists
#		-contains the day of the worked hours, and the number of hours worked for that day in descending date for the given employee
def get_id_employee_hours(employeeID):
	if not isinstance(employeeID, str):
		employeeID = str(employeeID)
	if(not employeeID.isdecimal()):
		return []
	q = "SELECT day, hours FROM SE_DB.hoursList WHERE employeeID = " + employeeID + " ORDER BY day DESC"
	c = db_util.db_open()
	hours = db_util.db_query(c, q)
	db_util.db_close(c)
	return hours


# input parameter(s):
#	employeeID
#		-an int
#		-represents the employee's ID
# return value:
#	hours
#		-a list of lists
#		-contains the employee ID, check in time, and check out time for days that a given employee has not checked out
def get_id_null_hours(employeeID):
	if not isinstance(employeeID, str):
		employeeID = str(employeeID)
	if(not employeeID.isdecimal()):
		return []
	q = "SELECT * FROM SE_DB.hours WHERE hours.checkOut is NULL and employeeID = " + employeeID + " LIMIT 1"
	c = db_util.db_open()
	hours = db_util.db_query(c, q)
	db_util.db_close(c)
	return hours


# input parameter(s): None
# return value:
#	hours
#		-a list of lists
#		-contains the employee ID, employee name, day, and hours for employees who have worked hours on the latest day
def get_latest_employee_hours():
	q = "SELECT  h.employeeID, h.employeeName, h.day, h.hours FROM SE_DB.hoursList h INNER JOIN (SELECT MAX(day) as maxDay FROM SE_DB.hoursList) m WHERE h.day = m.maxDay ORDER BY day DESC"
	c = db_util.db_open()
	hours = db_util.db_query(c, q)
	db_util.db_close(c)
	return hours


# input parameter(s):
#	employeeID
#		-an int
#		-represents the employee's ID
# return value: None
def add_checkout(employeeID):
	if not isinstance(employeeID, str):
		employeeID = str(employeeID)
	if(not employeeID.isdecimal()):
		return
	current_time = str(datetime.datetime.now())
	q = "UPDATE SE_DB.hours SET checkOut = '" + current_time + "' WHERE hours.checkOut is NULL and employeeID = " + employeeID + " LIMIT 1;" 
	c = db_util.db_open()
	db_util.db_execute(c, q)
	db_util.db_close(c)


# input parameter(s):
#	employeeID
#		-an int
#		-represents the employee's ID
# return value: None
def add_hours(employeeID):
	if not isinstance(employeeID, str):
		employeeID = str(employeeID)
	if(not employeeID.isdecimal()):
		return
	current_time = str(datetime.datetime.now())
	q = "INSERT INTO SE_DB.hours (employeeID, checkIn) VALUES (" + employeeID + ", '" + current_time + "');"
	c = db_util.db_open()
	db_util.db_execute(c, q)
	db_util.db_close(c)


##################################
# TRANSACTIONS RELATED FUNCTIONS #
##################################
# input parameter(s): None
# return value:
#	item_sales
#		-a list of lists
#		-contains date, item category, and the amount of sold in the item category on the specific date
def get_all_item_sales():
	q = "SELECT date, itemType, amountSold FROM SE_DB.salesCategories"
	c = db_util.db_open()
	item_sales = db_util.db_query(c, q)
	db_util.db_close(c)
	return item_sales


# input parameter(s): None
# return value:
#	money_sales
#		-a list of lists
#		-contains the date and amount of money made from sales that day
def get_all_money_sales():
	q = "SELECT day, totalSales FROM SE_DB.salesDaily"
	c = db_util.db_open()
	money_sales = db_util.db_query(c, q)
	db_util.db_close(c)
	return money_sales


###############################
#   LOGIN RELATED FUNCTIONS   #
############################### 
# input parameter(s):
# 	username
# 		-a string
#		-a user's username
# return value:
#	password
#		-a string
#		-the password for a given user's account or an empty string if it does not exist
def get_password(username):
	q = "SELECT password FROM SE_DB.logins WHERE username = '" + username + "';"
	c = db_util.db_open()
	password = db_util.db_query(c, q)
	db_util.db_close(c)
	if(len(password) == 1):
		return password[0][0]
	else:
		return ""


# input parameter(s):
# 	username
# 		-a string
#		-a user's username
# return value:
#	type
#		-a string
#		-the account type for a given user's account or an empty string if it does not exist
def get_account_type(username):
	q = "SELECT accountType FROM SE_DB.logins WHERE username = '" + username + "';"
	c = db_util.db_open()
	type = db_util.db_query(c, q)
	db_util.db_close(c)
	if(len(type) == 1):
		return type[0][0]
	else:
		return ""


# input parameter(s):
# 	username
# 		-a string
#		-a user's username
# return value:
#	id
#		-a string
#		-the ID for a given employee/manager user's account or an empty string if it does not exist or is not the proper account type
def get_id(username):
	q = "SELECT ID FROM SE_DB.logins WHERE username = '" + username + "';"
	c = db_util.db_open()
	id = db_util.db_query(c, q)
	db_util.db_close(c)
	if(len(id) == 1):
		return id[0][0]
	else:
		return ""


# input parameter(s):
#	username
#		-a string
#		-the username of the new account
#	password
#		-a string
#		-the username of the new account
#	accountType
#		-a string
#		-the account type of the new account
#	ID
#		-a string
#		-the employee ID of the new employee (if applicable)
#	first
#		-a string
#		-the first name of the new employee (if applicable)
#	last
#		-a string
#		-the last name of the new employee (if applicable)
# return value: None
def create_user(username, password, accountType, ID="NULL", first=None, last=None):
	q = "INSERT INTO SE_DB.logins (username, password, accountType, ID) VALUES ('" +username+ "','"+password+"','"+accountType+"',"+str(ID)+");"
	c = db_util.db_open()
	db_util.db_execute(c, q)
	if(first is not None and last is not None and ID != "NULL"):
		q = "INSERT INTO SE_DB.employees (lastName, firstName, ID, role) VALUES ('"+first+"','"+last+"',"+str(ID)+",'"+accountType+"');"
		db_util.db_execute(c, q)
	db_util.db_close(c)


##################################
# SHOPPINGLIST RELATED FUNCTIONS #
##################################
# input parameter(s):
#	user
#		-a string
#		-the username of the given user
# return value:
#	list
#		-a list of lists
#		-contains the name, price, and RFID of all items in a user's shopping list
def get_user_shopping_list(user):
	q = "SELECT name, price, item FROM SE_DB.userShoppingList WHERE username = \"" + user + "\""
	c = db_util.db_open()
	list = db_util.db_query(c, q)
	db_util.db_close(c)
	return list


# input parameter(s):
#	user
#		-a string
#		-the username of the given user
#	RFID
#		-an int
#		-the RFID of the item to be added
# return value: None
def add_slist_item(user, RFID):
	if not isinstance(user, str):
		user = str(user)
	if not isinstance(RFID, str):
		RFID = str(RFID)
	q = "INSERT INTO SE_DB.shoppingList(username, item) VALUES('" + user + "', '" + RFID + "');"
	c = db_util.db_open()
	db_util.db_execute(c, q)
	db_util.db_close(c)


# input parameter(s):
#	user
#		-a string
#		-the username of the given user
#	RFID
#		-an int
#		-the RFID of the item to be removed
# return value: None
def remove_slist_item(user, RFID):
	if not isinstance(user, str):
		user = str(user)
	if not isinstance(RFID, str):
		RFID = str(RFID)
	q = "DELETE FROM SE_DB.shoppingList WHERE username = \"" + user + "\" and item = " + RFID
	c = db_util.db_open()
	db_util.db_execute(c, q)
	db_util.db_close(c)


