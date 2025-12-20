from week4.decorators.ReportService import ReportService
from week4.decorators.UserService import UserService

admin_user = {
    "name": "Admin",
    "permissions": ["create_user", "generate_report"]
}

limited_user = {
    "name": "Viewer",
    "permissions": []
}

user_service = UserService(admin_user)
print(user_service.create_user("test@site.com"))

report_service = ReportService(admin_user)
print(report_service.generate_report())

