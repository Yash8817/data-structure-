stack = []


def pop():
    if not stack:
        print("Stack is empty!")
    else:
        removed_element = stack.pop()
        print("Removed element is :",removed_element)
        print(stack)


while True:
    print("Select option : 1.Push 2.Pop 3.Exit")
    ch = int(input("Enter choice:"))

    if ch == 1:
        push()
    elif ch == 2:
        pop()
    elif ch == 3:
        break
    else:
        print("Invalid choice !")



        
