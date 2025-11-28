print("***************************************************************************************************************")

print("Correct this below code with appropriate exception handlings. And finally print “Execution completed”")

def safe_divide(a,b):
    try :
        result = a / b
    except ZeroDivisionError as e :
        print("Exception :: ", e)
    except TypeError as e :
        print("Exception :: ", e)
    else :
        print(f"Result :: {result}")
    finally :
       print("Execution completed")

safe_divide(1,0)
safe_divide(1,"a")


print("***************************************************************************************************************")
