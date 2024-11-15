# from consumers.users_ms.user_consumer import *
# from consumers.tasks_ms.task_consumer import *
from consumers.reclamos_ms.reclamos_consumer import *

class RecordReclamosService:

    @staticmethod
    def create_record_reclamos_service(data):
        
        reclamo_data = {
                "id": data['id'],
                "details":{
                    "cliente_id": data['cliente_id'],
                    "description": data['description'],
                }
            }

        task = create_reclamos(reclamo_data)

        if task.status_code == 201:

            return True

        return False