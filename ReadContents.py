print("***************************************************************************************************************")

print("Write a Python program to read the entire content of a file named sample.txt and display it.")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

print("***************************************************************************************************************")
