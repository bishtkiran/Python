class Subscriber:
    active_user_count = 0

    def __init__(self, user_id: int, email: str, is_paid: bool):
        self.user_id = user_id
        self.email = email
        self.is_paid = is_paid
        self.active = True
        Subscriber.active_user_count += 1

    @staticmethod
    def is_valid_email(email: str) -> bool:
        return "@" in email and "." in email

    @classmethod
    def from_serialized(cls, data: str):
        user_id_str, email, plan = data.split("|")

        if not cls.is_valid_email(email):
            raise ValueError("Invalid email address")

        is_paid = plan.lower() == "paid"
        return cls(int(user_id_str), email, is_paid)
