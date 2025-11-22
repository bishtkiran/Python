print("***************************************************************************************************************")

print("1. Write a program that takes the input from the user and checks if a number is even or odd.")

num = int(input("Enter a number :: "))

if num % 2 == 0 :
    print("Entered number is an even number")
else :
    print("Entered number is an odd number")

print("***************************************************************************************************************")

print("2. Reverse a string using a for loop and check it is a palindrome. - Strings = “civic”, “hello”")

str_1 = 'civic'

reversed_str_1 = ''
for char in str_1:
    reversed_str_1 = char + reversed_str_1

if(str_1 == reversed_str_1):
    print("Pallindrome")
else :
    print("Not pallindrome")

print("***************************************************************************************************************")

print("3. Using the input from the user, Generate the first N numbers of the Fibonacci sequence.")

n = int(input("Enter the value of N: "))

result = []
a = 0
b = 1

for _ in range(n) :
    result.append(a)
    temp = a
    a = b
    b = temp + b

print(result)

print("***************************************************************************************************************")

print("4. From list [1,2,3,4,5]. Write code to find two values from the list when added the result is 9.	#Expected output : [4, 5]")

list = [1, 2, 3, 4, 5]

result = 9

for i in range(len(list)) :
    for j in range(i + 1, len(list)) :
        if list[i] + list[j] == result :
            print([list[i], list[j]])
            break

print("***************************************************************************************************************")

print("5. Print all even numbers between 1 and 20 using a while loop.")

count = 2
while count <= 20:
    print(count)
    count = count + 2

print("***************************************************************************************************************")

print("6. Find the first occurrence of a number in a list and stop further searching.")

numbers = [10, 20, 30, 40, 50]
search_for = 30

for i in range(len(numbers)) :
    if numbers[i] == search_for:
        print(numbers[i], i)
        break

print("***************************************************************************************************************")

print("7. Using continue statement, print only the odd numbers from 1 to 10.")

for i in range(10):
    if i % 2 == 1 :
        print(i)
    else:
        continue

print("***************************************************************************************************************")

print("8. What will be the output ")

for i in range(5):
    if i == 3:
        pass
    print(i)

# Output : 0 1 2 3 4

print("***************************************************************************************************************")

print("9. Write a program that takes a day of the week as input and prints whether it's a weekday or weekend using match conditional statements.")

def day_of_week(day) :
    match day :
        case "Saturday" | "Sunday" :
            return "It's Weekend"
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" :
            return "It is a Weekday"
        case _ :
            return "Enter a valid day"

print(day_of_week("Monday"))

print("***************************************************************************************************************")
