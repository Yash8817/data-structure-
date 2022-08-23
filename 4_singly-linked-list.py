class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end="")
                n = n.ref
                
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head =new_node

    def add_end(self,data):
        new_node = Node(data)

        if self.head is None:
            print("Linkedlist is empty")
        else:
            n = self.head

            while n.ref is not None:
                n = n.ref

            n.ref = new_node
    def add_after(self,data,x):
        n = self.head

        while n is not None:
            if n.data == x:
                break
            n = n.ref

        if n is None:
            print(data,"not present in linkedlist")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Linkedlist is empty")
            return

        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref

        if n.ref is None:
            print(data,"not present in linkedlist")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("linkedllist is empty")
        else:
            self.head =self.head.ref

    def delete_end(self):
        if self.head is None:
            print("linkedlist is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:    
                 n = n.ref
            n.ref = None
    def delete_by_value(self,x):
        if self.head is None:
            print("linkedlist is empty")
            return

        if self.head.data == x:
            self.head = self.head.ref
            return

        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("can't delete, LL is empty")
        else:
            n.ref = n.ref.ref

LL1=LinkedList()
while True:
    print("\n")
    print("|------- Linkedlist programs --------|")
    print("1.Traverse LL")
    print("2.add element at beggining")
    print("3.add element at end")
    print("4.add element at before element ")
    print("5.add element at after element ")
    print("6.delete from beggining")
    print("7.delete from end")
    print("8.delete from by value")
    print("9.exit")
    ch = int(input("Enter choice:"))
    if ch == 1:
        LL1.print_LL()
    elif ch == 2:
        element = int(input("Enter value you want add at beggining:"))
        LL1.add_begin(element)
    elif ch == 3:
        element = int(input("Enter value you want add at end:"))
        LL1.add_end(element)
    elif ch == 4:
        x = int(input("before which element you want to add :"))
        element = int(input("Enter value you want add before:"))
        LL1.add_before(element,x)
    elif ch == 5:
        x = int(input("after which element you want to add :"))
        element = int(input("Enter value you want add before:"))
        LL1.add_after(element,x)
    elif ch == 6:
        LL1.delete_begin()
    elif ch == 7:
        LL1.delete_end()
    elif ch == 8:
        value = int(input("Enter value you want delete:"))
        LL1.delete_by_value(value)
    elif ch == 9:
        break
    else:
        print("Invalid choice:")
        
