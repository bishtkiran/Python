print("***************************************************************************************************************")

print("From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.")

def read_file_generator(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line


for line in read_file_generator("myfile.txt"):
    print(line)

print("***************************************************************************************************************")
