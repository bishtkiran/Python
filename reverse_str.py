print("Write a function that takes one parameter as a string and reverse it and return.")

def reverse_string(string) :
    reversed_string = ''

    for char in string :
        reversed_string = char + reversed_string
    return reversed_string

print(reverse_string("Kiran"))
