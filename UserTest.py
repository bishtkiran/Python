from week4.FreeUser import FreeUser
from week4.PaidUser import PaidUser
from week4.User import User

free_user = FreeUser(1, "preeti.singh@gmail.com")
paid_user = PaidUser(2, "pradeep.singh@gmail.com", "12345","credit_card")
paid_user_2 = PaidUser(3, "kirti.singh@gmail.com", "87636","debit_card")

print(free_user.can_use_feature("download_content"))
print(paid_user.can_use_feature("download_content"))

print(paid_user.is_subscription_active())

paid_user.cancel_subscription()
print(paid_user.is_subscription_active())

print(User.active_user_count)

paid_user.deactivate();

print(User.active_user_count)
