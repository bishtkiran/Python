from collections import namedtuple

UserConfig = namedtuple("UserConfig", ["max_features", "plan_name"])

class User:
    def __init__(self, user_id: int, email: str, config: UserConfig):
        self.user_id = user_id
        self.email = email
        self._config = config

    def get_plan_name(self) -> str:
        return self._config.plan_name

    def can_add_feature(self, current_feature_count: int) -> bool:
        return current_feature_count < self._config.max_features

FREE_CONFIG = UserConfig(max_features=2, plan_name="Free")
PAID_CONFIG = UserConfig(max_features=10, plan_name="Paid")

free_user = User(1, "free.user@gmail.com", FREE_CONFIG)
paid_user = User(2, "paid.user@gmail.com", PAID_CONFIG)

print(free_user.get_plan_name())
print(paid_user.get_plan_name()) 


