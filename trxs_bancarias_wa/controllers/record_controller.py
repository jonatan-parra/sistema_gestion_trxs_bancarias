from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.record_service import RecordService
from services.record_reclamo_service import RecordReclamoService
from services.record_gestion_service import RecordGestionService
from services.record_user_service import RecordUserService

record_api = Blueprint('record_api', __name__)

@record_api.route('/record', methods=['POST'])
def create_record():

    data = request.form
    name = data.get('name')
    last_name = data.get('last_name')
    email = data.get('email')
    role = data.get('role')
    is_active = data.get('is_active')


    task_id = data.get('task_id')
    task_name = data.get('task_name')
    task_description = data.get('task_description')

    if not name:
        return jsonify({'error': 'User name is required'}), 400

    if not last_name:
        return jsonify({'error': 'last_name is required'}), 400
    
    if not task_name:
        return jsonify({'error': 'Task name is required'}), 400

    RecordService.create_record(name, last_name, email, role, is_active, task_id, task_name, task_description)
    return redirect(url_for('record_api.index'))

@record_api.route('/record_reclamo', methods=['POST'])
def create_record_reclamo():

    data = request.form
    id = data.get('id')
    cliente_id = data.get('cliente_id')
    description = data.get('description')

    RecordReclamoService.create_record_reclamo(id, cliente_id, description)
    return redirect(url_for('record_api.index'))

@record_api.route('/record_gestion', methods=['POST'])
def create_record_gestion():

    data = request.form
    id = data.get('id')
    user_id = data.get('user_id')
    id_trx = data.get('id_trx')
    tipo_de_fraude = data.get('tipo_de_fraude')
    description = data.get('description')
    acciones = data.get('acciones')

    RecordGestionService.create_record_gestion(id, user_id, id_trx, tipo_de_fraude, description, acciones)
    return redirect(url_for('record_api.index'))


@record_api.route('/record_user', methods=['POST'])
def create_record_user():

    data = request.form
    name = data.get('name')
    last_name = data.get('last_name')
    email = data.get('email')
    role = data.get('role')
    is_active = data.get('is_active')

    RecordUserService.create_record_user(name, last_name, email, role, is_active)
    return redirect(url_for('record_api.index'))





@record_api.route('/')
def index():
    return render_template('index.html')

@record_api.route('/reclamo')
def reclamo():
    return render_template('reclamo.html')


@record_api.route('/gestion')
def gestion():
    return render_template('gestion.html')


@record_api.route('/usuario')
def usuario():
    return render_template('usuario.html')


