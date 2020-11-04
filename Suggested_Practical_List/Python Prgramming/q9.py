queue = []
def push(n):
    queue.append(n)
def pop():
    if len(queue)>0:
        return queue.pop(0)
while True:
    print("Queue Menu")
    print("1. push")
    print("2. pop")
    print("0. exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        n = int(input("Enter a number to push: "))
        push(n)
        print("Element pushed")
    elif choice == 2:
        n = pop()
        if n is None:
            print("No more elements.")
        else:
            print("Popped value is: ",n)
    elif choice == 0:
        break
    else:
        print("Invalid choice")
print("Bye")
