from functools import reduce

print("***************************************************************************************************************")

print("1. Given a list let's see how to double each element of the given list. Using map()")

a = [1, 2, 3, 4]

squares = list(map(lambda x : x * 2, a))
print(squares)

print("***************************************************************************************************************")

print("2. Use filter() and lambda to extract all even numbers from a list of integers.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x : x % 2 == 0, numbers))
print(evens)

print("***************************************************************************************************************")

print("3. Use reduce() and lambda to find the longest word in a list of strings. From functools import reduce")

words = ["apple", "banana", "cherry", "date"]

longest = reduce(lambda x, y: x if len(x) >= len(y) else y, words)
print(longest)

print("***************************************************************************************************************")

print("4. Use map() to square each number in the list and round the result to one decimal place.")

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

square_floats = list(map(lambda x : round( x ** 2, 1), my_floats))
print(square_floats)

print("***************************************************************************************************************")

print("5. Use filter() to select names with 7 or fewer characters from the list.")

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

name = list(filter(lambda name : len(name) <= 7 , my_names))
print(name)

print("***************************************************************************************************************")

print("6. Use reduce() to calculate the sum of all numbers in a list. [1, 2, 3, 4, 5]")

list = [1, 2, 3, 4, 5]

sum_of_nums = reduce(lambda sum, num : sum + num, list)
print(sum_of_nums)

print("***************************************************************************************************************")





