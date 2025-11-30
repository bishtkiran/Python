import csv

print("***************************************************************************************************************")

print("Write a Python program to create a CSV file named students.csv with columns Name, Roll Number, and Marks. Add at least three entries")

data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("***************************************************************************************************************")
