import functions_framework

from google.cloud import firestore

db = firestore.Client(project="cbse-2024ii-438703", database="reclamos_db")

@functions_framework.http
def gestiones_api(request):

    if request.method == 'POST':

        data = request.get_json()

        doc = db.collection("reclamos").document(data['id'])
        doc.set(data['details'])

    return 'Reclamo creado con id={}'.format(data['id']), 201