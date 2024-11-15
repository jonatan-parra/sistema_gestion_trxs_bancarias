from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.record_service import RecordService

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

@record_api.route('/')
def index():
    return render_template('index.html')