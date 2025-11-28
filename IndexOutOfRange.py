print("***************************************************************************************************************")

print("Apply exception handling to below code and handle an exception if the index is out of range")

my_list = [1, 2, 3]

try :
    print(my_list[5])
except IndexError as e :
    print("Exception :: ", e)

print("***************************************************************************************************************")
