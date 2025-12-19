from week4.User import User

class PaidUser(User):
    PAID_FEATURES = {
        "browse_content",
        "playback",
        "search",
        "download_content",
        "ad_free_experience"
    }

    def __init__(self, user_id: int, email: str, package_id: str, payment_method: str):
        super().__init__(user_id, email)
        self.payment_method = payment_method
        self.package_id = package_id
        self.subscription_active = True

    def is_subscription_active(self) -> bool:
        return self.subscription_active

    def can_use_feature(self, feature_name: str) -> bool:
        return self.subscription_active and feature_name in self.PAID_FEATURES

    def cancel_subscription(self):
        self.subscription_active = False
