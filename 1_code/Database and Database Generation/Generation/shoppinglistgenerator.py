## Written by: Kimberly Chang
## Tested by: Kimberly Chang
## Debugged by: Kimberly Chang

import random
import datetime

import util

items = util.parse_csv("items.csv", 0)
# util.print_nested_list(items)

customerIDs = ["katie587", "coolcat53", "lakes", "laura", "LeaAnderson", "jjohnson", "flyingpigs43", "ilovecats", "amy67", "roger23"]

shopping_list = [["username", "item"]]
for customer in customerIDs:
	no = random.randint(1, 30)
	insert = []
	for j in range(0, no):
		insert.append(customer)

		i = random.randint(1, 10000)

		# items(name, brand, type, RFID, price)
		insert.append(items[i][3])

		shopping_list.append(insert)

		insert = []

util.print_nested_list(shopping_list)

util.write_csv("shoppingList.csv", shopping_list)