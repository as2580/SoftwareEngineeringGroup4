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
    q = "SELECT * FROM SE_DB.tasks WHERE state = \"Complete\";"
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
    q = "SELECT * FROM SE_DB.tasks WHERE state != \"Complete\";"
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


###########################
# ITEMS RELATED FUNCTIONS #
########################### 
# input parameter(s): 
#	RFID
#		-an int
#		-represents the item's RFID
# return value:
#	tasks
#		-a list of lists
#		-contains the item with matching RFID
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
#	
def get_items():
	q = "SELECT name, brand, price FROM SE_DB.items"
	c = db_util.db_open()
	info = db_util.db_query(c, q)
	db_util.db_close(c)
	return info
	
def get_search_result(query):
	q = "SELECT name, brand, price, RFID FROM SE_DB.items WHERE name like \"%" + query +"%\""
	c = db_util.db_open()
	info = db_util.db_query(c, q)
	db_util.db_close(c)
	return info


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
def get_all_employee_hours():
	q = "SELECT employeeID, employeeName, day, hours FROM SE_DB.hoursList ORDER BY day DESC"
	c = db_util.db_open()
	hours = db_util.db_query(c, q)
	db_util.db_close(c)
	return hours


def get_latest_employee_hours():
	q = "SELECT  h.employeeID, h.employeeName, h.hours, h.day FROM SE_DB.hoursList h INNER JOIN (SELECT MAX(day) as maxDay FROM SE_DB.hoursList) m WHERE h.day = m.maxDay ORDER BY day DESC"
	c = db_util.db_open()
	hours = db_util.db_query(c, q)
	db_util.db_close(c)
	return hours


##################################
# TRANSACTIONS RELATED FUNCTIONS #
##################################
def get_all_item_sales():
	q = "SELECT date, itemType, amountSold FROM SE_DB.salesCategories"
	c = db_util.db_open()
	item_sales = db_util.db_query(c, q)
	db_util.db_close(c)
	return item_sales

	
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
#
# return value:
#	
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
#
# return value:
#	
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
#
# return value:
#	
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
#
# return value:
#	
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

def get_user_shopping_list(user):
	q = "SELECT name, price, item FROM SE_DB.userShoppingList WHERE username = \"" + user + "\""
	c = db_util.db_open()
	list = db_util.db_query(c, q)
	db_util.db_close(c)
	return list

def add_slist_item(user, RFID):
	if not isinstance(user, str):
		user = str(user)
	if not isinstance(RFID, str):
		RFID = str(RFID)
	q = "INSERT INTO SE_DB.shoppingList(username, item) VALUES('" + user + "', '" + RFID + "');"
	c = db_util.db_open()
	db_util.db_execute(c, q)
	db_util.db_close(c)

	
def remove_slist_item(user, RFID):
	if not isinstance(user, str):
		user = str(user)
	if not isinstance(RFID, str):
		RFID = str(RFID)
	q = "DELETE FROM SE_DB.shoppingList WHERE username = \"" + user + "\" and item = " + RFID
	c = db_util.db_open()
	db_util.db_execute(c, q)
	db_util.db_close(c)


