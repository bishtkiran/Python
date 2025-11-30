print("***************************************************************************************************************")

print("Create a decorator cache that caches the result of a function based on its arguments.")

def cache(func):
    cache_store = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))

        if key in cache_store:
            return cache_store[key]

        result = func(*args, **kwargs)
        cache_store[key] = result            
        return result

    return wrapper


@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x

print(expensive_computation(5))
print(expensive_computation(5))
print(expensive_computation(5))
print(expensive_computation(5))

print("***************************************************************************************************************")
