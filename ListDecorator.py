import time

print("***************************************************************************************************************")

print(" Write a function that appends 1 to 1000 numbers to a list and add a decorator to that function to calculate the start and end time. Calculate the total time taken and print.")

def calculate_start_end_time(func) :
    def wrapper() :
        start_time = time.time()
        func()
        end_time = time.time()
        time_taken = start_time + end_time
        print(time_taken)
    return  wrapper

@calculate_start_end_time
def append_digits() :
    list = []
    for i in range(1, 1001) :
        list.append(i)

append_digits()

print("***************************************************************************************************************")
