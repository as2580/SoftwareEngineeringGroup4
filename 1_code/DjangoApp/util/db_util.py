import util.lib.mysql.connector


h = "anna-336.cqxst1sb3a0a.us-east-2.rds.amazonaws.com"
p = 3306
un = "admin"
pw = "SoftwareEngineeringProject"


def db_open():
	connection = util.lib.mysql.connector.connect(
		host=h,
		port=p,
		user=un,
		password=pw)
	return connection


def db_close(connection):
	connection.close()


def db_query(connection, query):
	cursor = connection.cursor()
	cursor.execute(query)
	output = cursor.fetchall()
	cursor.close()
	return output


def db_execute(connection, query):
	cursor = connection.cursor()
	cursor.execute(query)
	connection.commit()
	cursor.close()


def print_output(output):
	for line in output:
		print(line)
