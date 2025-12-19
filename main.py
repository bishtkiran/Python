from week4.Subscriber import Subscriber

print(Subscriber.is_valid_email("test@example.com"))
print(Subscriber.is_valid_email("my-test-email"))


serialized_user = "101|paid_user@example.com|paid"

user = Subscriber.from_serialized(serialized_user)

print(user.user_id)
print(user.email)
print(user.is_paid)

