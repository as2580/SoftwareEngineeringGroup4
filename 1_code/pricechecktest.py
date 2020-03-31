# NOTE:
# This is just a demo. Features such as the RFID scanner and the Items Database
# have not yet been implemented. Thus, they are being simulated through an
# input text field (rfid scanner) and a pre-made list of Items (database)
# Additionally, the methods used to create a user interface will likely not be used in the final version

import tkinter as tk

#setting up UI
root = tk.Tk()
canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()
root.title("PRICE CHECKER (e.g. 00000, lo6dk, cc1?1)")
entry1 = tk.Entry(root, bd=1)
entry1.insert(0, 'RFID scanner')
entry1.config(fg = 'grey')
canvas1.create_window(200, 140, window=entry1)

# Object to hold info about an item (database entry)
class Item:
    def __init__(self, rfid, price):
        self.rfid = rfid
        self.price = price


# getprice requests from 'database' an item with the given rfid
def getprice():
    i = entry1.get()
    price = -1

    for item in I:
        if(i == item.rfid):
            price = item.price
    if price>=0:
        label1 = tk.Label(root, text='                The price of this item is $' + str(price) + '                ')
    else:
        label1 = tk.Label(root, text='Error detecting item. Please scan again')

    canvas1.create_window(200, 230, window=label1)

# input field polish
def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if entry1.get() == 'RFID scanner':
       entry1.delete(0, "end") # delete all the text in the entry
       entry1.insert(0, '') #Insert blank for user input
       entry1.config(fg = 'black')

def on_focusout(event):
    if entry1.get() == '':
        entry1.insert(0, 'RFID scanner')
        entry1.config(fg = 'grey')


entry1.bind('<FocusIn>', on_entry_click)
entry1.bind('<FocusOut>', on_focusout)
button1 = tk.Button(text='Scan', command=getprice)
canvas1.create_window(200, 180, window=button1)



I = [] #database
I.append(Item('aaaa2', 10.99))
I.append(Item('aaaaa', 6.25))
I.append(Item('ii2jc', 19.99))
I.append(Item('cc1?1', 0.50))
I.append(Item('bbbb3', 12.00))
I.append(Item('asdfg', 50.00))
I.append(Item('lo6dk', 630.00))
I.append(Item('11111', 1.00))
I.append(Item('22222', 2.22))
I.append(Item('33333', 3.03))
I.append(Item('55555', 5.50))
I.append(Item('99999', 99.99))
I.append(Item('rfid0', 12000.00))
I.append(Item('12345', 15.00))
I.append(Item('00000', 100.00))

# message to instruct user
label1 = tk.Label(root, text='Scan an item to check its price!')
canvas1.create_window(200, 230, window=label1)

# display ui
root.mainloop()