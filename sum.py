print("Write a Python function that takes two parameters as lists and to sum all the numbers in a list. ")

def sum(list1, list2) :
    sum = 0

    for i in range(len(list1)) :
        sum += list1[i]

    for j in range(len(list2)) :
        sum += list2[j]

    return sum

a = [8, 2, 3, 0, 7]
b =  [3, -2, 5, 1]
result = sum(a, b)
print(result)
