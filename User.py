from abc import ABC, abstractmethod

class User(ABC):
    active_user_count = 0

    def __init__(self, user_id: int, email: str):
        self.user_id = user_id
        self.email = email
        self.active = True
        User.active_user_count += 1

    def deactivate(self):
        if self.active:
            self.active = False
            User.active_user_count -= 1

    def is_subscription_active(self) -> bool:
        return False

    @abstractmethod
    def can_use_feature(self, feature_name: str) -> bool:
        pass
