import functools
import time


def log_execution(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time

        print(
            f"[LOG] {func.__name__} | "
            f"args={args[1:] if len(args) > 1 else args} | "
            f"kwargs={kwargs} | "
            f"duration={duration:.4f}s"
        )

        return result

    return wrapper

def conditional_logger(enabled: bool = True):

    def decorator(func):
        if not enabled:
            return func

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG ENABLED] Calling {func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    return decorator

class UserService:

    @log_execution
    def create_user(self, user_id: int, email: str):
        return {"user_id": user_id, "email": email}

    @conditional_logger(enabled=True)
    def deactivate_user(self, user_id: int):
        return f"User {user_id} deactivated"

    @conditional_logger(enabled=False)
    def internal_health_check(self):
        return "OK"


service = UserService()

service.create_user(1, "test.user@example.com")

service.deactivate_user(1)

service.internal_health_check()



