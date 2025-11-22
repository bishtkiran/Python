print("Write a recursive function to compute the factorial of a non-negative integer.")

def fact(n) :
    if n == 0 | n == 1 :
        return n
    else :
        return  n * fact(n - 1)

print(fact(5))
