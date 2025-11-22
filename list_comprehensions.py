print("***************************************************************************************************************")

print("1. Given a list of numeric strings, convert them into integers. Using List Comprehensions")

strings = ["1", "2", "3", "4", "5"]

num_list = [int(string) for string in strings]
print(num_list)

print("***************************************************************************************************************")

print("2. Extract all integers from a list that are greater than 10. Using List Comprehensions")

numbers = [1, 5, 13, 4, 16, 7]

nums_list = [num for num in numbers if num > 10]
print(nums_list)

print("***************************************************************************************************************")

print("3. Create a list of squares for numbers from 1 to 5. Using List Comprehensions")

nums = [1, 2, 3, 4, 5]

squares = [num * num for num in nums]
print(squares)

print("***************************************************************************************************************")

print("4. Convert a 2D list into a 1D list.Using List Comprehensions")

matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]

list =[num for list in matrix for num in list]

print(list)

print("***************************************************************************************************************")

print("5. Given two lists, keys = ['a', 'b', 'c'] and values = [1, 2, 3], create a dictionary using dictionary comprehension.")

keys = ['a', 'b', 'c']
values = [1, 2, 3]

dict = {keys[i] : values[i] for i in range(len(keys))}
print(dict)

print("***************************************************************************************************************")

print("6. Given the dictionary scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}, create a new dictionary containing only the students who scored above 80")

scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}

new_scores = {student : score for student, score in scores.items() if score > 80}
print(new_scores)

print("***************************************************************************************************************")
