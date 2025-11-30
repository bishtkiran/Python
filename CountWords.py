print("***************************************************************************************************************")

print("Write a Python program to count the number of words in a file named words.txt")

with open("words.txt", "r") as file:
    content = file.read()
    words = content.split()
    print("Number of words:", len(words))

print("***************************************************************************************************************")
