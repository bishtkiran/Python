class UserRepository:
    def __init__(self, users: list[dict]):
        self._users = users

    def iter_active_users(self):
        for user in self._users:
            if user.get("active"):
                yield user

users = [
    {"id": 1, "email": "ankit.kumar@gmail.com", "active": True},
    {"id": 2, "email": "brijesh.singh@gmail.com", "active": False},
    {"id": 3, "email": "diya.kumari@gmail.com", "active": True},
    {"id": 4, "email": "gaurav.bhatt@gmail.com", "active": True},
]

repo = UserRepository(users)

active_users = repo.iter_active_users()

print(next(active_users))

for user in active_users:
    print(user)


