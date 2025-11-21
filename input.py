print("***************************************************************************************************************")

print("Write a program that asks the user for their name and then prints a greeting   message using their name.")

name = input("Enter you name. ")
greeting = 'Good Morning'

print(greeting + ', ' + name)

print("***************************************************************************************************************")

print("Ask the user to enter two numbers from the user and print their sum, multiplication, and division.")

num_1 = int(input("Enter the first number "))

num_2 = int(input("Enter the second number "))

print("Sum = " + str(num_1 + num_2))

print("Product = " + str(num_1 * num_2))

print("Division = " + str((num_1 / num_2)))

print("***************************************************************************************************************")

print("Ask the user to enter input names separated by commas, split the string from comma and copy to a list and print.")

names = input("Enter comma separated names ")

list = names.split(",")

print(list)

print("***************************************************************************************************************")

print("Ask the user to enter their age and check if they are eligible to vote based on their age.")

age = int(input("Enter you age. "))

if age >= 18 :
    print("You are eligible to vote")
else :
    print("You are not eligible to vote")

print("***************************************************************************************************************")

print("For value = 3.14159, Using f-string print output for only up to 2 decimal places.")

val = 3.14159

print(f"{val:.2f}")

print("***************************************************************************************************************")
