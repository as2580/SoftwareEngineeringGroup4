## Written by: Kimberly Chang
## Tested by: Kimberly Chang
## Debugged by: Kimberly Chang

import random
import datetime

import util


def rand_datetime(start_date, end_date, rh, rm):
	time_between_dates = end_date - start_date
	days_between_dates = time_between_dates.days
	random_number_of_days = random.randrange(days_between_dates)
	random_date = start_date + datetime.timedelta(days=random_number_of_days)
	random_datetime = datetime.datetime(random_date.year, random_date.month, random_date.day, rh, rm)
	return random_datetime


def rand_date(start_date, end_date):
	time_between_dates = end_date - start_date
	days_between_dates = time_between_dates.days
	random_number_of_days = random.randrange(days_between_dates)
	random_date = start_date + datetime.timedelta(days=random_number_of_days)
	return random_date


# DATABASE SCHEMA
# items(name, brand, type, RFID, price)                                                     IMPLEMENTED
# stock(itemRFID, amt, expirationDate, location)                                            _
# employees(lastName, firstName, ID, role)                                                  IMPLEMENTED
# hours(employeeID, day, checkIn, checkOut, dayHours)                                       _
# tasks(taskName, description, taskID, state, employeeID, timeCreated, timeCompleted)       implemented
# sales(transactionID, time, totalPaid)                                                     _
# transactions(transactionID, time, item, amt)                                              _
# logins(username, password, accountType)                                                   IMPLEMENTED

items = util.parse_csv("items.csv", 0)
# util.print_nested_list(items)

employees = util.parse_csv("employees.csv", 0)
# util.print_nested_list(employees)

# CREATING THE STOCK CSV

stock = [["itemRFID", "amt", "expirationDate", "location"]]
stock_item_no = util.parse_csv("random_items_numbers.csv", 0)
# util.print_nested_list(stock_item_no)

sin_len = len(stock_item_no[0])-1
sin_half_len = sin_len/2
for i in range(0, sin_len):
	insert = []
	sin = int(stock_item_no[0][i])
	# stock(itemRFID, amt, expirationDate, location)

	# BACK ROOM
	# itemRFID
	item_RFID = items[sin][3]
	insert.append(item_RFID)

	# amt
	amt = random.randint(0, 2000)
	insert.append(amt)

	# expirationDate
	day1 = datetime.date(2020, 1, 1)
	day2 = datetime.date(2025, 12, 31)
	random_hour = random.randint(0, 23)
	random_min = random.randint(0, 59)
	date = rand_datetime(day1, day2, random_hour, random_min)
	insert.append(date)

	# location
	insert.append("Back Room")

	# adding line into table
	stock.append(insert)
	insert = []

	# STORE STOCK
	# itemRFID
	item_RFID = items[sin][3]
	insert.append(item_RFID)

	# amt
	amt = random.randint(0,1000)
	insert.append(amt)

	# expirationDate
	day1 = datetime.date(2020, 1, 1)
	day2 = datetime.date(2022, 12, 31)
	random_hour = random.randint(0, 23)
	random_min = random.randint(0, 59)
	date = rand_datetime(day1, day2, random_hour, random_min)
	insert.append(date)

	# location
	item_type = items[sin][2]
	item_loc = ""
	if item_type == "Fruit" or item_type == "Vegetable":
		item_loc = "Produce"
	elif item_type == "Frozen":
		item_loc = "Aisle 9"
	elif item_type == "Dairy":
		item_loc = "Aisle 8"
	elif item_type == "Grain":
		item_loc = "Aisle 7"
	elif item_type == "Meat":
		item_loc = "Aisle 6"
	elif item_type == "Drink":
		item_loc = "Aisle 5"
	elif item_type == "Health":
		item_loc = "Aisle 4"
	elif item_type == "Beauty":
		item_loc = "Aisle 3"
	elif item_type == "Bath":
		item_loc = "Aisle 2"
	else:  # Electronics
		item_loc = "Aisle 1"
	insert.append(item_loc)

	# adding line into table
	stock.append(insert)

# util.print_nested_list(stock)

util.write_csv("stock.csv", stock)

# CREATING THE HOURS CSV
hours = [["employeeID", "day", "checkIn", "checkOut", "dayHours"]]
for i in range(0, 999):
	insert = []
	# hours(employeeID, day, checkIn, checkOut, dayHours)

	# employeeID
	emID = random.randint(1, 60)
	insert.append(emID)

	# day
	day1 = datetime.date(2010, 1, 1)
	day2 = datetime.date(2022, 12, 31)
	date = rand_date(day1, day2)
	insert.append(date)

	# checkIn
	in_hour = random.randint(1, 20)
	in_min = random.randint(0, 59)
	in_time = datetime.time(hour=in_hour, minute=in_min)
	insert.append(in_time)

	# checkOut
	out_time = None
	out_hour = None
	out_min = random.randint(0, 59)
	if random.randint(0, 1) == 1:
		if in_hour >= 17:
			out_hour = in_hour + random.randint(1, 3)
		else:
			out_hour = in_hour + random.randint(1, 6)
		out_time = datetime.time(hour=out_hour, minute=out_min)
	insert.append(out_time)

	# dayHours
	day_hour = None
	day_min = None
	employ_hours = None
	if out_time is not None:
		day_hour = out_hour - in_hour
		day_min = out_min - in_min
		if day_min < 0:
			day_hour = day_hour - 1
			day_min = 60 + day_min
		employ_hours = day_hour + (day_min/60)
	insert.append(employ_hours)

	# adding line into table
	hours.append(insert)

# util.print_nested_list(hours)

util.write_csv("hours.csv", hours)

# CREATING THE SALES AND TRANSACTIONS SALES CSV
sales = [["transactionID", "time", "totalPaid"]]
transactions = [["transactionID", "time", "item", "amt"]]
t_year = random.randint(1990,2019)
t_month = random.randint(1,12)
t_day = random.randint(1,28)
t_hour = random.randint(0,23)
t_min = random.randint(0,59)
t_id = 1
for i in range(0, 99):
	s_insert = [t_id]
	# sales(transactionID, time, totalPaid)
	# transactions(transactionID, time, item, amt)

	# sales - time
	t_datetime = datetime.datetime(t_year, t_month, t_day, t_hour, t_min)
	s_insert.append(t_datetime)

	# sale - totalPaid
	price_sum = 0
	no_items = random.randint(1, 30)
	these_items = random.sample(range(1, 10000), no_items)
	for j in range(0, no_items):
		t_insert = []
		# items(name, brand, type, RFID, price)
		this_rfid = int(items[these_items[j]][3])
		this_price = float(items[these_items[j]][4])
		this_amt = random.randint(1, 10)
		# transactions - transactionID
		t_insert.append(t_id)
		# transactions - time
		t_insert.append(t_datetime)
		# transactions - item
		t_insert.append(this_rfid)
		# transactions - amt
		t_insert.append(this_amt)
		# inserting into table
		transactions.append(t_insert)
		# calculation for sales
		price_sum = price_sum + (this_price*this_amt)

	price_sum = price_sum*1.07  # "tax"
	s_insert.append(price_sum)

	sales.append(s_insert)

	# updating the date and t_id
	t_id = t_id + 1
	day_inc = random.randint(0, 1)
	if day_inc == 1:
		t_day = t_day + day_inc
		t_id = 1
		# 28 days: 2
		# 30 days: 4, 6, 9, 11
		# 31 days: 1, 3, 5, 7, 8, 10, 12
		if (t_month == 2 and t_day > 28) or (t_month in [4, 6, 9, 11] and t_day > 30) or (
				t_month in [1, 3, 5, 7, 8, 10, 12] and t_day > 31):
			t_month = t_month + 1
			t_day = 1
			if t_month > 12:
				t_month = 1
	else:
		min_inc = random.randint(1, 1000)
		if min_inc > 60:
			t_hour = t_hour + int(min_inc/60)
			min_inc = min_inc % 60
			if t_hour > 23:
				t_hour = t_hour - 24
				t_day = t_day + 1
				t_id = 1
				if (t_month == 2 and t_day > 28) or (t_month in [4, 6, 9, 11] and t_day > 30) or (
						t_month in [1, 3, 5, 7, 8, 10, 12] and t_day > 31):
					t_month = t_month + 1
					t_day = 1
					if t_month > 12:
						t_month = 1

# print("SALES\n-----------------------")
# util.print_nested_list(sales)
# print("\nTRANSACTIONS\n-----------------------")
# util.print_nested_list(transactions)


util.write_csv("sales.csv", sales)
util.write_csv("transactions.csv", transactions)


