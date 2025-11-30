print("***************************************************************************************************************")

print("2. Write a generator function called infinite_multiples(n) that yields multiples of the given base value indefinitely.")

def infinite_multiples(n):
    count = 1
    while True:
        yield n * count
        count += 1

gen = infinite_multiples(3)

for _ in range(5):
    print(next(gen))

print("***************************************************************************************************************")
