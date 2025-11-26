print("***************************************************************************************************************")

print("1. Check if All Numbers are Positive. Given a list of integers, determine if all numbers are positive. Using all()")

numbers = [1, 2, 3, 4, 5]

print(all(x > 0 for x in numbers))

print("***************************************************************************************************************")

print("2. Check if Any Number is Even. Given a list of integers, check if any number is even. Using any()")

numbers = [1, 3, 5, 7, 8]

print(any(x % 2 == 0 for x in numbers))

print("***************************************************************************************************************")

print("3. Determine if any number in a list is divisible by 5 an print.")

list = [7, 9, 6, 15, 12, 17 ]

number = any(num % 5 == 0 for num in list)
print(number)

print("***************************************************************************************************************")


