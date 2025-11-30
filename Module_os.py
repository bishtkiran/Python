import os
from datetime import datetime, timedelta

print("***************************************************************************************************************")

print("Using datetime,add a week and 12 hours to a date.  Given date: March 22, 2020, at 10:00 AM. print original date time and new date time")

original_date = datetime(2020, 3, 22, 10, 0)

time_to_add = timedelta(weeks = 1, hours = 12)

new_date = original_date + time_to_add

print("Original Date ::", original_date)
print("New Date ::", new_date)

print("***************************************************************************************************************")

print("Code to get the dates of yesterday, today, and tomorrow.")

today_date = datetime.now().date()

yesterday_date = today_date - timedelta(days=1)

tomorrow_date = today_date + timedelta(days=1)

print("Yesterday Date ::", yesterday_date)
print("Today Date ::", today_date)
print("Tomorrow Date ::", tomorrow_date)

print("***************************************************************************************************************")

print("Write a code snippet using os module, to get the current working directory and print and create a folder “test”. List all the files and folders in the current working directory and remove the directory “test” that was created.")

cwd = os.getcwd()
print("Current working directory is ::", cwd)

folder_name = "test"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created.")
else:
    print(f"Folder '{folder_name}' already exists.")

print("Files and folders in current directory:")
for item in os.listdir(cwd):
    print(item)

if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"Folder '{folder_name}' removed.")

print("***************************************************************************************************************")

print("Write a Python program to rename a file from old_name.txt to new_name.txt.")

old_name = "myfile.txt"
new_name = "my_file.txt"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"File renamed from '{old_name}' to '{new_name}'")
else:
    print(f"File '{old_name}' does not exist.")

print("***************************************************************************************************************")

print("Create a file and Write a Python program to get the size of a file named example.txt ")

with open("example.txt", "w") as file:
    file.write("Example file created successfully.\nIt's good learning about python modules and OS.\nHappy Learning.")

file_size = os.path.getsize("example.txt")
print(f"Size of 'example.txt': {file_size} bytes")

print("***************************************************************************************************************")

print("Convert the string \"Feb 25 2020 4:20PM\" into a Python datetime object")

date_str = "Feb 25 2020 4:20PM"
dateObj = datetime.strptime(date_str, "%b %d %Y %I:%M%p")
print(dateObj)

print("***************************************************************************************************************")

print("Subtract 7 days from the date 2025-02-25 and print the result.")

dateObj = datetime.strptime("2025-02-25", "%Y-%m-%d").date()
new_date = dateObj - timedelta(days = 7)
print("New date:", new_date)

print("***************************************************************************************************************")

print("Format the date 2020-02-25 as \"Tuesday 25 February 2020\"")

dateObj = datetime.strptime("2020-02-25", "%Y-%m-%d")
formatted_date = dateObj.strftime("%A %d %B %Y")
print(formatted_date)

print("***************************************************************************************************************")





