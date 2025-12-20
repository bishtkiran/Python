import time

from week4.decorators.decorator import time_execution, require_permission


class UserService:
    def __init__(self, current_user: dict):
        self.current_user = current_user

    @time_execution
    @require_permission("create_user")
    def create_user(self, email: str):
        time.sleep(0.1)  # simulate work
        return f"User {email} created"
