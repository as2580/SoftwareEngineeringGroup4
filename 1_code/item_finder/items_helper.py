import db_util

def get_price(RFID):
    q = "SELECT price FROM items WHERE rfid = RFID;"
    c = db_util.db_open()
    price = db_util.db_query(c, q)
    return price

def get_name(RFID):
    q = "SELECT name FROM items WHERE rfid = RFID;"
    c = db_util.db_open()
    name = db_util.db_query(c, q)
    return name

def get_shelved(RFID):
    pass

def get_shelved(name):
    pass

def get_all_items():
    q = "SELECT * FROM SE_DB.items;"
    c = db_util.db_open()
    items = db_util.db_query(c, q)
    db_util.db_close(c)
    return items

print('The price of this item is $' + get_price('cf?ed'))