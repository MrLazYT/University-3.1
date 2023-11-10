import random

arr = list()

for i in range(10):
    arr.append(random.randint(1, 10))

print("List values: ")

for i in range(10):
    print(f"{arr[i]}, ", end = "")

print("\n")