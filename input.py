name = input("Enter you name. ")
greeting = 'Good Morning'

print(greeting + ', ' + name)

print("***********************")

num_1 = int(input("Enter the first number "))

num_2 = int(input("Enter the second number "))

print("Sum = " + str(num_1 + num_2))

print("Product = " + str(num_1 * num_2))

print("Division = " + str((num_1 / num_2)))

print("***********************")

names = input("Enter comma separated names ")

list = names.split(",")

print(list)

print("***********************")

age = int(input("Enter you age. "))

if age >= 18 :
    print("You are eligible to vote")
else :
    print("You are not eligible to vote")

print("***********************")

val = 3.14159

print(f"{val:.2f}")

print("***********************")
