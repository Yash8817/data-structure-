class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class doublyLL:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end="")
                n = n.nref

    def print_LL_reverse(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data ,"-->" , end=" ")
                n = n.pref

    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("linkedlist is not empty")

    def add_begin(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head  = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head  = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref = new_node
            new_node.pref = n

    def add_after(self,data,x):
        if self.head is None:
            print("linkedlist is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("item not present in linkedlist")
            else:
                new_node=Node(data)
                new_node.nref = n.pref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = n
                n.nref = new_node

    def add_before(self,data,x):
        if self.head is None:
            print("linkedlist is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("item not present in linkedlist")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head=new_node 
                
                n.pref = new_node
                    
    def delete_begin(self):
        if self.head is None:
            print("linkedlist is empty")
            return

        n= self.head

        if n.nref is None:
            self.head = None
            return
        else:
            self.head = n.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("linkedlist is empty")
            return
        n= self.head

        if n.nref is None:
            self.head = None
        else:
            while n.nref is not None:
                n = n.nref
            n.pref.nref= None
        
    def delete_by_value(self,x):
        if self.head is None:
            print("linkedlist is empty")
            return
        n = self.head

        if n.nref is None:
            if n.data == x:
                self.head=None
            else:
                print("item not present in data")
                return
        if n.data == x:
            self.head = n.nref
            self.head.pref = None
            return

        while n.nref is not None:
            if n.data == x:
                break
            n= n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("item not present in linkedlist")
  
dl1 =doublyLL()
while True:
    print("\n")
    print("|------- Doubly Linkedlist programs --------|")
    print("1.Traverse DLL")
    print("2.Reverse traverse DLL")
    print("3.Insert into empty DLL")
    print("4.add element at beggining")
    print("5.add element at end")
    print("6.add element at after element ")
    print("7.add element at before element ")
    print("8.delete from beggining")
    print("9.delete from end")
    print("10.delete from by value")
    print("11.exit")
    ch = int(input("Enter choice:"))
    if ch == 1:
        dl1.print_LL()

    elif ch== 2:
        dl1.print_LL_reverse()

    elif ch== 3:
        elemnt= int(input("Enter item you want to insert:"))
        dl1.insert_empty(elemnt)

    elif ch== 4:
        elemnt= int(input("Enter item you want to at beggining:"))
        dl1.add_begin(elemnt)

    elif ch== 5:
        elemnt= int(input("Enter item you want to at end:"))
        dl1.add_end(elemnt)

    elif ch== 6:
        pos= int(input("after which item you want to add:"))
        elemnt= int(input("Enter item you want to add:"))
        dl1.add_after(elemnt,pos)

    elif ch== 7:
        pos= int(input("before which item you want to add:"))
        elemnt= int(input("Enter item you want to add:"))
        dl1.add_before(elemnt,pos)

    elif ch== 8:
        dl1.delete_begin()

    elif ch== 9:
        dl1.delete_end()

    elif ch== 10:
        elemnt= int(input("Enter item you want to delete:"))
        dl1.delete_by_value(elemnt)
    elif ch == 11:
        break
    else:
        print("invalid choice:")
