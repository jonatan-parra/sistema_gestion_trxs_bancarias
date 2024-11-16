from consumers.users_ms.user_consumer import *

class RecordService:

    @staticmethod
    def create_record_user_service(data):

        user_data = {
            "name": data['name'],
            "last_name": data['last_name'],
            "email": data['email'],
            "role": data['role'],
            "is_active": data['is_active'],
        }

        user = create_user(user_data)

        return True