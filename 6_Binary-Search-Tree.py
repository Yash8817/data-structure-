class BST:
    def __init__(self,key):
        self.key = key
        self.lchild= None
        self.rchild= None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return

        #for duplicate data
        if self.key == data:
            return

        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild  =BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild  =BST(data)
    
    def search(self,data):
        if self.key == data:
            print("node is present")
            return
        
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("node is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node is not present")
            
        
    def preorder(self):
        print(self.key , end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key , end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key , end=" ")

    def min_node(self):
        current= self
        while current.lchild:
            current  = current.lchild
        print("Smallest node value:",current.key)

    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("Maximum node value:",current.key)
    
    def delete(self,data,curr):
        if self.key is None:
            print("tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print("node not present ")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print("node not present")
        else:
            
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self= None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self= None
                return temp
            node =self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,curr)
        return self
    
def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)
        
    
root = BST(10)
while True:
    print()
    print("|------------TREE------------|")
    print("1.insert node in tree")
    print("2.search for node in tree")
    print("3.view pre-order traversal")
    print("4.view in-order traversal")
    print("5.view post-order traversal")
    print("6.delete node from tree")
    print("7.view maximum node value")
    print("8.view minimum node value")
    print("9.exit")
    print("|-----------------------------|")
    ch = int(input("Enter your choice:"))
    if ch==1:
        val = int(input("enter space seprated value"))
        root.insert(val)
        root.inorder()
    elif ch == 2:
        val = int(input("Enter value you want to seach:"))
        root.search(val)
    elif ch == 3:
        print("pre-order traversa")
        root.preorder()
    elif ch == 4:
        print("in-order traversa")
        root.inorder()
    elif ch == 5:
        print("post-order traversa")
        root.postorder()
    elif ch == 6:
        val = int(input("Enter value you want to delete:"))
        if count(root)>1:
            root.delete(val,root.key)
        else:
            print("deletion is not posible")
            root.inorder()
            
    elif ch == 7:
        root.min_node()
    elif ch == 8:
        root.max_node()
    elif ch == 9:
        break
    else:
        print("invalid choice")
        
        
            
