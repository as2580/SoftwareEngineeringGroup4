# This program help custmors find an item they want in the store

# items in the store
items=["Bread", "Suger", "Chips", "Cereal", "Frozen Pizza", "Eggs", "Milk", "Apple", "Banana", "Salt"] 
# asile number 
asile=[1,2,3,4,5]
# section number  
section=[1,2,3]

# function checks if item is in stock 
def inStock(itemName):
    for i in range(0,len(items)):   # the for loop goes through the all items in the store
        if items.index(i)==0:       # the if statement check if the item searched by the custmor is in stock       
            return 0            # prints out true if that item is not in stock
        else:
            return 1           # if the item is in stock than it returns FaLse

# function that gives asile and section number for an item in the store
def itemLocator(itemName):          
    for i in range(0,len(items)):     # the for loop goes through the all the items
        for j in range(0,len(asile)):            # this for loop goes through the all the asiles
            for y in range(0,len(section)):      # this for loop goes through the all the sections
                if items[i]==itemName & inStock(itemName)==0:       # the if statement checks if the an item searched by custmors 
                                                                     # is in the list
                                                                     # ALso, if that item is in stock than it will proceed
                    result=asile[j]+[i]      # the asile and section number
                    print(result)            # prins the asile and section number 
                else:
                    print("Item out of Stock")    # else it prints out the item is out of stock
                    break 
            
name=print(input("Enter a item:"))  # custmors input an item they want to find the location for 
itemLocator(name)                   # calls the function itemLocator
   
