from consumers.record_consumer import *

class RecordService:

    @staticmethod
    def create_record(name, last_name, email, role, is_active, task_id, task_name, task_description):

        # data = {
        #     "name": "Jonatan wa",
        #     "last_name":"Parra",
        #     "email": "correo@unal.edu.co",
        #     "role": "Ingeniero",
        #     "is_active":1,
        #     "task_id": "abc-123-4500",
        #     "task_name": "Tarea 1",
        #     "task_description": "Clase de ISBN 2024ii"
        # }

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