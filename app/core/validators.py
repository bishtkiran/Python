class FeatureValidator:
    def __init__(self, allowed_features: list[str]):
        self.allowed_features = allowed_features

    def validate(self, feature: str):
        for allowed in self.allowed_features:
            if allowed == feature:
                return True
        else:
            raise ValueError("Feature not provided")
