from functools import wraps
from datetime import datetime

def lifecycle_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cls_name = args[0].__class__.__name__
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {cls_name}.{func.__name__}() called")
        return func(*args, **kwargs)

    return wrapper

class User:
    def __init__(self, user_id: int, email: str):
        self.user_id = user_id
        self.email = email

    def __str__(self):
        return f"User(id={self.user_id}, email={self.email})"


class Subscriber(User):

    active_user_count = 0

    def __init__(self, user_id: int, email: str, is_paid: bool):
        super().__init__(user_id, email)
        self.is_paid = is_paid
        self.active = True
        Subscriber.active_user_count += 1

    def __repr__(self):
        return (
            f"Subscriber(user_id={self.user_id}, "
            f"email='{self.email}', "
            f"is_paid={self.is_paid}, "
            f"active={self.active})"
        )

    @lifecycle_logger
    def deactivate(self):
        if self.active:
            self.active = False
            Subscriber.active_user_count -= 1

    @lifecycle_logger
    def activate(self):
        if not self.active:
            self.active = True
            Subscriber.active_user_count += 1

    def __del__(self):
        if self.active:
            Subscriber.active_user_count -= 1
        print(f"Subscriber {self.user_id} deactivated")

    def __enter__(self):
        print(f"Entering context for Subscriber {self.user_id}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exiting context for Subscriber {self.user_id}")
        self.deactivate()

def active_subscribers(subscribers):
    for sub in subscribers:
        if sub.active:
            yield sub


def print_subscribers(subscribers):
    print("\n********** Subscriber Details **********")
    for sub in subscribers:
        print(
            f"Subscriber ID={sub.user_id:<3} | "
            f"Subscriber Email={sub.email:<25} | "
            f"Is Paid Subscriber={str(sub.is_paid):<5} | "
            f"Is Active Subscriber={str(sub.active):<5}"
        )

    print(f"\n ********** Active subscriber count :: {Subscriber.active_user_count}")


def main():
    print("******************** Entry Point ***************************\n")

    subscribers = [
        Subscriber(1, "kiran@gmail.com", True),
        Subscriber(2, "bisht@yahoo.com", False),
        Subscriber(3, "kandari@gmail.com", True),
    ]

    print_subscribers(subscribers)

    print("\n********** Active Subscribers using generator **********")
    for sub in active_subscribers(subscribers):
        print(f"→ {sub}")

    print("\n***** Context Manager *****")
    with Subscriber(4, "kiran@gmail.com", False) as temp_sub:
        print(f"Inside context :: {temp_sub}")

    print(f"\n ***** Active subscriber count after context :: {Subscriber.active_user_count}")

    print("\n********** Deactivating Subscriber 1 **********")
    subscribers[0].deactivate()

    print_subscribers(subscribers)

    print("\n********** Exit **********\n")


if __name__ == "__main__":
    main()
