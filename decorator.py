import time
import functools


def time_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[TIMER] {func.__name__} took {(end - start):.4f}s")
        return result
    return wrapper

def require_permission(required_permission: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user = getattr(args[0], "current_user", None)

            if not user or required_permission not in user.get("permissions", []):
                raise PermissionError(
                    f"Permission '{required_permission}' required"
                )

            return func(*args, **kwargs)
        return wrapper
    return decorator

