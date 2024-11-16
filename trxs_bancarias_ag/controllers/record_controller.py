from flask import Blueprint, request, jsonify
from services.record_service import RecordService
from services.record_reclamos_service import RecordReclamosService
from services.record_gestiones_service import RecordGestionesService

record_api = Blueprint('record_api', __name__)

@record_api.route('/api/record', methods=['POST'])
def create_record_controller():

    data = request.get_json()

    response = RecordService.create_record_service(data)

    if response == True:
        return jsonify("Record has been successfully created."), 201

    return jsonify("Error al guardar"), 400


@record_api.route('/api/record_reclamo', methods=['POST'])
def create_record_reclamos_controller():

    data = request.get_json()

    response = RecordReclamosService.create_record_reclamos_service(data)

    if response == True:
        return jsonify("Record has been successfully created."), 201

    return jsonify("Error al guardar"), 400


@record_api.route('/api/record_gestion', methods=['POST'])
def create_record_gestiones_controller():

    data = request.get_json()

    response = RecordGestionesService.create_record_gestiones_service(data)

    if response == True:
        return jsonify("Record has been successfully created."), 201

    return jsonify("Error al guardar"), 400