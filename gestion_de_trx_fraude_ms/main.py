import functions_framework

from google.cloud import firestore

db = firestore.Client(project="isbn-2024i", database="gestiones_db")

@functions_framework.http
def gestiones_api(request):

    if request.method == 'POST':

        data = request.get_json()

        doc = db.collection("gestiones").document(data['id'])
        doc.set(data['details'])

    return 'Gestión creada con id={}'.format(data['id']), 201