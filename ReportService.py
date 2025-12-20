import time

from week4.decorators.decorator import time_execution, require_permission


class ReportService:
    def __init__(self, current_user: dict):
        self.current_user = current_user

    @time_execution
    @require_permission("generate_report")
    def generate_report(self):
        time.sleep(0.2)  # simulate work
        return "Report generated"
