print("***************************************************************************************************************")

print("Create a parameterised decorator retry that retries a function a specified number of times.")

def retry(no_of_times):
    def parameterized_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(no_of_times):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return parameterized_decorator


@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")

may_fail("Shivani")

print("***************************************************************************************************************")
