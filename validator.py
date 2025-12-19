class Validator:
    def __init__(self, allowed_features: list[str]):
        self.allowed_features = allowed_features

    def validate_feature(self, feature: str):
        for allowed in self.allowed_features:
            if allowed == feature:
                print("Feature allowed")
                break
        else:
            raise ValueError("Feature not allowed")
