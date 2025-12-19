from week4.User import User

class FreeUser(User):
    FREE_FEATURES = {"browse_content", "search"}

    def can_use_feature(self, feature_name: str) -> bool:
        return feature_name in self.FREE_FEATURES
