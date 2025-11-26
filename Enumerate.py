print("***************************************************************************************************************")

print("1. Using below list and enumerate(), print index followed by value. ")

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

print("***************************************************************************************************************")

print("2. Using below dict and enumerate, print key followed by value")

person = {"name": "Alice", "age": 30, "city": "New York"}

for index, (key, value) in enumerate(person.items()) :
    print(f"{key}: {value}")

print("***************************************************************************************************************")

print("3. Given the list, use enumerate() to create a list of tuples where each tuple contains the index and the corresponding fruit, but only for even indices.")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruit_list = [(i, fruit) for i, fruit in enumerate(fruits, start = 1) if i % 2 == 0]
print(fruit_list)

print("***************************************************************************************************************")
