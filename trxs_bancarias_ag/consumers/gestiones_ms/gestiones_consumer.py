import requests

from config import ISBN_GESTIONES_MS_API_URL

base_url = ISBN_GESTIONES_MS_API_URL

# Create Task
def create_gestiones(data):

    url = base_url

    response = requests.post(url, json=data)

    return response