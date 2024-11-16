import requests

from config import ISBN_AG_API_URL

base_url = ISBN_AG_API_URL

# Create Record
def create_record(data):

    url = base_url + '/api/record'

    response = requests.post(url, json=data)

    return response

# Create Reclamo
def create_record_reclamo(data):

    url = base_url + '/api/record_reclamo'

    response = requests.post(url, json=data)

    return response

# Create Gestion
def create_record_gestion(data):

    url = base_url + '/api/record_gestion'

    response = requests.post(url, json=data)

    return response