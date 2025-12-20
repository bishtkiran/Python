from week4.app.core.models import User
from week4.app.services.feature_service import FeatureService
from week4.app.core.validators import FeatureValidator


def main():
    validator = FeatureValidator(
        allowed_features=["browse", "search", "download"]
    )

    service = FeatureService(validator)
    user = User(user_id=1, features=[])

    service.enable_feature_for_user(user, "browse")
    print(user.features)


if __name__ == "__main__":
    main()
