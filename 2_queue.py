queue = []

def enqueue():
    element = int(input("Enter element:"))
    queue.append(element)

def dequeue():
    if not queue:
        print("Queue is empty:")
    else:
        element = queue.pop(0)
        print("Removed element is ",element)
        print(queue)

def display():
    print(queue)
    



while True:
    print("Select option: 1.add 2.remove 3.show 4.exit")
    ch = int(input("Enter choice:"))
    if ch == 1:
        enqueue()
    elif ch ==2:
        dequeue()
    elif ch ==3:
        display()
    elif ch == 4:
        break
    else:
        print("Invalid option")
