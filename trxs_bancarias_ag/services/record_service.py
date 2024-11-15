from consumers.users_ms.user_consumer import *
from consumers.tasks_ms.task_consumer import *

class RecordService:

    @staticmethod
    def create_record_service(data):
        print("Entra en create_record_service")

        user_data = {
            "name": data['name'],
            "last_name": data['last_name'],
            "email": data['email'],
            "role": data['role'],
            "is_active": data['is_active'],
        }

        print("Entra en user_data")


        user = create_user(user_data)

        if user.status_code == 201:

            task_data = {
                "id": data['task_id'],
                "details":{
                    "name": data['task_name'],
                    "description": data['task_description'],
                    "user_id": "1"
                }
            }

            task = create_task(task_data)

            if task.status_code == 201:

                return True

        return False