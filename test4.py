import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from fastapi import FastAPI
import re

cred = credentials.Certificate(".\\.gitignore\\first-test-2fc42-firebase-adminsdk-2limr-9396562c62.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
app = FastAPI()

def save_detail(save_data):
    try:
        room_id = str((save_data.keys()))[12:-3]
        detail_ref = db.collection('rooms').document(room_id)
        detail_ref.set(
            save_data[room_id]
        )
    except Exception as e:
        print(e)
        return False
    else:
        return True
    
@app.post("/test00")
def test00(item : dict):
    return save_detail(item)

@app.get("/test11")
def test11(room_id: str):
    room_ref = db.collection('rooms').document(room_id)
    return room_ref.get().to_dict()