print("***************************************************************************************************************")

print("Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.")

def validate_positive(function) :
    def wrapper(x) :
        if x <= 0 :
            return "Argument passed is not positive!!"
        return function(x)
    return wrapper

@validate_positive
def square_root(x):
    return x ** 0.5

print(square_root(-3))

print("***************************************************************************************************************")
