import requests

from config import ISBN_RECLAMOS_MS_API_URL

base_url = ISBN_RECLAMOS_MS_API_URL

# Create Task
def create_reclamos(data):

    url = base_url

    response = requests.post(url, json=data)

    return response