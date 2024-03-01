import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from fastapi import FastAPI

cred = credentials.Certificate(".\\.gitignore\\first-test-2fc42-firebase-adminsdk-2limr-9396562c62.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
app = FastAPI()

@app.get("/testusers/{user_id}")
def user_detail(user_id):
    doc = db.collection(u'test users').document(user_id)
    user_data = doc.get().to_dict()
    return user_data