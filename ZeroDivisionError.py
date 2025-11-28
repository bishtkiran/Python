print("***************************************************************************************************************")

print("Write a Python program that attempts to divide two numbers and handles a ZeroDivisionError if the denominator is zero. Divide a by b and handle the exception and print the error")

a = 10
b = 0

try :
    c = a / b
except ZeroDivisionError as e :
    print("Exception :: ", e)
else :
    print(c)

print("***************************************************************************************************************")
