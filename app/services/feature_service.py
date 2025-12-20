from week4.app.core.models import User
from week4.app.core.validators import FeatureValidator


class FeatureService:
    def __init__(self, validator: FeatureValidator):
        self.validator = validator

    def enable_feature_for_user(self, user: User, feature: str):
        self.validator.validate(feature)
        user.features.append(feature)
        return user
