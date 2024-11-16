from consumers.gestiones_ms.gestiones_consumer import *

class RecordGestionesService:

    @staticmethod
    def create_record_gestiones_service(data):
        
        reclamo_data = {
                "id": data['id'],
                "details":{
                    "user_id": data['user_id'],
                    "id_trx": data['id_trx'],
                    "tipo_de_fraude": data['tipo_de_fraude'],
                    "description": data['description'],
                    "acciones": data['acciones'],
                }
            }

        task = create_gestiones(reclamo_data)

        if task.status_code == 201:
            return True

        return False