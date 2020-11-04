import random
while True:
    x = input("Press ENTER to roll the dice (any other key to exit): ")
    if len(x) > 0:
        break
    n = random.randint(1,6)
    print(n)
print("Bye")
