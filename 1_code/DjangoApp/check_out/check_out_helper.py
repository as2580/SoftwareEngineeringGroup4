class Node(object):

    def __init__(self, name=None, price=None, next_node=None):
        self.name = name
        self.price = price
        self.next_node = next_node

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, name, price):
        new_node = Node(name, price)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, name):
        current = self.head
        found = False
        while current and found is False:
            if current.get_name() == name:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("name not in list")
        return current

    def delete(self, name):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_name() == name:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("name not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


# test code

