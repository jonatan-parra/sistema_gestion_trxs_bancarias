import functions_framework

from google.cloud import firestore

db = firestore.Client(project="cbse-2024ii-438703", database="gestiones-db")

@functions_framework.http
def gestiones_api(request):

    if request.method == 'POST':

        data = request.get_json()

        doc = db.collection("gestiones").document(data['id'])
        doc.set(data['details'])

    return 'Gestión creada con id={}'.format(data['id']), 201