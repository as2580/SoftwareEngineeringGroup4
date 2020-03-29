import task_board.db_util as db_util
import datetime


# input parameter(s): None
# return value:
#   tasks
#       -a list of lists
#       -contains all tasks
#       -nested list is a tuple containing all information for a given tasks
def get_all_tasks():
    q = "SELECT * FROM SE_DB.tasks;"
    c = db_util.db_open()
    tasks = db_util.db_query(c, q)
    db_util.db_close(c)
    return tasks


# input parameter(s): taskID
# return value:
#   task
#       -a tuple containing all information for a given tasks
def get_task(taskID):
    q = "SELECT * FROM SE_DB.tasks WHERE taskID = " + taskID + ";"
    c = db_util.db_open()
    task = db_util.db_query(c, q)
    db_util.db_close(c)
    return task
	

# input parameter(s):
#   employee_id
#       -an int
#       -represents the employee's ID
# return value:
#   employee
#       -a list
#       -contains the employee's last name at employee[0] and the employee's first name at employee[1]
def get_employee(employee_id):
    q = "SELECT lastName, firstName FROM SE_DB.employees WHERE ID = " + str(employee_id) + ";"
    c = db_util.db_open()
    employee = db_util.db_query(c, q)
    db_util.db_close(c)
    return employee


# input parameter(s): None
# return value:
#   tasks
#       -a list of lists
#       -contains only tasks that are Complete
#       -nested list is a tuple containing all information for a given tasks
def get_completed_tasks():
    q = "SELECT * FROM SE_DB.tasks WHERE state = \"Complete\";"
    c = db_util.db_open()
    tasks = db_util.db_query(c, q)
    db_util.db_close(c)
    return tasks


# input parameter(s): None
# return value:
#   tasks
#       -a list of lists
#       -contains only tasks that are not Complete
#       -nested list is a tuple containing all information for a given tasks
def get_noncompleted_tasks():
    q = "SELECT * FROM SE_DB.tasks WHERE state != \"Complete\";"
    c = db_util.db_open()
    tasks = db_util.db_query(c, q)
    db_util.db_close(c)
    return tasks


# input parameter(s): None
# return value:
#   tasks
#       -a list of lists
#       -contains only tasks that are In Progress
#       -nested list is a tuple containing all information for a given tasks
def get_inprogress_tasks():
    q = "SELECT * FROM SE_DB.tasks WHERE state = \"In Progress\";"
    c = db_util.db_open()
    tasks = db_util.db_query(c, q)
    db_util.db_close(c)
    return tasks


# input parameter(s): None
# return value:
#   tasks
#       -a list of lists
#       -contains only tasks that are Incomplete
#       -nested list is a tuple containing all information for a given tasks
def get_incomplete_tasks():
    q = "SELECT * FROM SE_DB.tasks WHERE state = \"Incomplete\";"
    c = db_util.db_open()
    tasks = db_util.db_query(c, q)
    db_util.db_close(c)
    return tasks


# input parameter(s):
#   title
#       -a string
#       -represents the title/name of the task
#   description
#       -a string
#       -represents the description of the tasks
# return value: None
def add_task(title, description):
    current_time = str(datetime.datetime.now())
    q = "INSERT INTO SE_DB.tasks(taskName, description, state, timeCreated) VALUES(\'" + title
    q = q + "/', /'" + description + "/'," + "/'Incomplete/'," + current_time + ");"
    c = db_util.db_open()
    db_util.db_execute(c, q)
    db_util.db_close(c)


# input parameter(s):
#   title
#       -a string
#       -represents the title/name of the task
#   creation_time
#       -a datetime
#       -represents the time that the task was created
#   new_state
#       -a string
#       -contains the state to which the task's state should be changed
#   employee
#       -an int
#       -contains the employee's ID if the state is being changed to "In Progress"
#       -otherwise, should be None
# return value: None
def update_task_state(title, creation_time, new_state, employee):
    q = "UPDATE SE_DB.employees SET state = \"" + new_state + "\""
    if new_state == "Complete":
        current_time = str(datetime.datetime.now())
        q = q + ", timeCompleted = " + current_time
    elif new_state == "In Progress":
        q = q + ", employeeID = " + employee
    q = q + " WHERE taskName = " + title + " AND timeCreated = " + creation_time + ";"
    c = db_util.db_open()
    db_util.db_execute(c, q)
    db_util.db_close(c)


def modify_task(taskID, taskName=None, description=None, state=None, employeeID=None, timeCreated=None, timeCompleted=None):
	q = "UPDATE SE_DB.employees SET taskName = \"" + taskName + "\""
	q = q + ", description = \"" + description + "\""
	q = q + ", state = \"" + state + "\""
	q = q + ", employeeID = \"" + employeeID + "\""
	q = q + ", timeCreated = \"" + timeCreated + "\""
	q = q + ", timeCompleted = \"" + timeCompleted + "\""
	q = q + " WHERE taskID = " + taskID + ";"
	c = db_util.db_open()
	db_util.db_execute(c, q)
	db_util.db_close(c)

# db_util.print_output(get_employee(1))

