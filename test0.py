http://127.0.0.1:8000/items/5?q=somequery

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from fastapi import FastAPI

cred = credentials.Certificate(".\\.gitignore\\first-test-2fc42-firebase-adminsdk-2limr-9396562c62.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
app = FastAPI()

users_ref = db.collection(u'test users')
docs = users_ref.stream()

doc_ref = db.collection(u'test users').document(u'users01')
doc_ref.set({
    u'name': u'試験',
    u'university': u'大学',
    u'grade': 3,
    u'hobby' : u'趣味'
})


for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/testusers/{user_id}")
def user_detail(user_id):
    doc_r = db.collection(u'test users').document(user_id)
    user_data = doc_r.get().to_dict()
    return user_data