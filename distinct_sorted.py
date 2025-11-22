print("Write a Python function that takes a list and returns a new list with distinct and sorted elements from the first list.")


def distint_sorted_elements(list) :
    distinct_ele = set()
    for i in range(len(list)) :
        distinct_ele.add(list[i])

    return sorted(distinct_ele)

a = [4, 1, 2, 3, 3, 1, 3, 4, 5, 1, 7]
set = distint_sorted_elements(a)
print(set)

