from functools import total_ordering

@total_ordering
class User:
    active_user_count = 0

    def __init__(self, user_id: int, email: str, is_paid: bool, features: list[str]):
        self.user_id = user_id
        self.email = email
        self.is_paid = is_paid
        self.features = features
        self.active = True
        User.active_user_count += 1

    def __str__(self):
        plan = "Paid" if self.is_paid else "Free"
        return f"User {self.user_id} ({plan}) - {self.email}"

    def __repr__(self):
        return (
            f"User(user_id={self.user_id}, "
            f"email='{self.email}', "
            f"is_paid={self.is_paid}, "
            f"features={self.features})"
        )

    def __len__(self):
        return len(self.features)

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.user_id == other.user_id


    def __lt__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.is_paid < other.is_paid

    def __call__(self, feature_name: str) -> bool:
        return feature_name in self.features
