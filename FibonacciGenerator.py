print("***************************************************************************************************************")

print("1.Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers Of 10  numbers")

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci = fibonacci_generator()

for _ in range(10):
    print(next(fibonacci))

print("***************************************************************************************************************")
