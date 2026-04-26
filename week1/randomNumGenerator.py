import random

print("generate a random number between two nums")
x = input("Enter the lower bound: ")
y = input("Enter the upper bound: ")
random_number = random.randint(int(x), int(y))
print("The random number generated is: " + str(random_number))