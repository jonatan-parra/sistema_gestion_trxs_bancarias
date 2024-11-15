from consumers.record_consumer import *

class RecordReclamoService:

    @staticmethod
    def create_record_reclamo(id, cliente_id, description):
        data = {
            "id": id,
            "cliente_id": cliente_id,
            "description": description,
        }

        return create_record_reclamo(data)