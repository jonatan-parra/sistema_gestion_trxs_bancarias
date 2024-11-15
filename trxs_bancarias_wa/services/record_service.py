from consumers.record_consumer import *

class RecordService:

    @staticmethod
    def create_record(name, last_name, email, role, is_active, task_id, task_name, task_description):
        data = {
            "name": name,
            "last_name": last_name,
            "email": email,
            "role": role,
            "is_active": 1,
            "task_id": task_id,
            "task_name": task_name,
            "task_description": task_description
        }

        return create_record(data)