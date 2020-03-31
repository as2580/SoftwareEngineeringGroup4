import util.lib.mysql.connector


h = "anna-336.cqxst1sb3a0a.us-east-2.rds.amazonaws.com"
p = 3306
un = "admin"
pw = "SoftwareEngineeringProject"


# creates a connection to the database that MUST BE CLOSED with db_close()
def db_open():
	connection = util.lib.mysql.connector.connect(
		host=h,
		port=p,
		user=un,
		password=pw)
	return connection


# closes the connection to the database
def db_close(connection):
	connection.close()


# queries the database for an SQL query that returns results
# returns such results as a list of lists where each nested lsit represents a tuple
def db_query(connection, query):
	cursor = connection.cursor(buffered=True)
	cursor.execute(query)
	output = cursor.fetchall()
	cursor.close()
	return output


# queries the database for an SQL query that does not return results
def db_execute(connection, query):
	cursor = connection.cursor(buffered=True)
	cursor.execute(query)
	connection.commit()
	cursor.close()


# prints the output of a list
def print_output(output):
	for line in output:
		print(line)
