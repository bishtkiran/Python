print("***************************************************************************************************************")

print("Create a decorator requires_permission that checks if a user has the ‘admin’ permission before allowing access to a function, if a different user then responds “Access denied”.")

def requires_permission(func):
    def wrapper(user, *args, **kwargs):
        if 'admin' in user.get('permissions', []):
            return func(user, *args, **kwargs)
        else:
            print("Access denied!!")
    return wrapper

@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")

admin = {'name': 'Raj', 'permissions': ['admin']}
hr = {'name': 'Kirti', 'permissions': ['HR']}

delete_user(admin, 100)
delete_user(hr, 200)

print("***************************************************************************************************************")
