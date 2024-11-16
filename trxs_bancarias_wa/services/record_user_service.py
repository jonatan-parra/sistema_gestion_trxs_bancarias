from consumers.record_consumer import *

class RecordUserService:

    @staticmethod
    def create_record_user(name, last_name, email, role, is_active):
        data = {
            "name": name,
            "last_name": last_name,
            "email": email,
            "role": role,
            "is_active": 1,
        }

        return create_record_user(data)