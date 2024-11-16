from consumers.record_consumer import *

class RecordGestionService:

    @staticmethod
    def create_record_gestion(id, user_id, id_trx, tipo_de_fraude, description, acciones):
        data = {
            "id": id,
            "user_id": user_id,
            "id_trx": id_trx,
            "tipo_de_fraude":tipo_de_fraude,
            "description":description,
            "acciones":acciones,
        }

        return create_record_gestion(data)