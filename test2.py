import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from fastapi import FastAPI
import re

cred = credentials.Certificate(".\\.gitignore\\first-test-2fc42-firebase-adminsdk-2limr-9396562c62.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
app = FastAPI()

test00 = ['table', 3, 4, 5,6]
number = 2

def save(**user_datil):
    user_datil_ref = db.collection(u'rooms').document(user_datil['room_id'])
    remove_room_id = user_datil.pop('room_id')
    user_datil_ref.set({
        user_datil['furniture_name']:user_datil
    })
    user_datil['room_id'] = remove_room_id
    return True


test02 ={'room_id':'oo', 'furniture_name':'box', 'position':{1, 2}, 'size':20, 'rote':30}
print(test02)
@app.get("/test02/{user_datil}")
def test02_test():
    return (save(**test02))

@app.get("/")
def test():
    return {"Hello": "World"}

@app.get("/test")
def test_save():
    test_ref = db.collection(u'rooms').document(u'test@gmail.com_1')
    user_data = test_ref.get().to_dict()
    return(user_data)

test01 = {'furniture_name':'chair', 'position':{0, 1}, 'size':10, 'rote':20}

@app.get("/test00")
def test01():
    test01_ref = db.collection(u'rooms').document(u'test00@gmail.com_1')
    test01_ref.set({
        'chair': test01
    })
    return('fin')

def dict_test(test):
    print(test)
    return



@app.get("/romtes/{item}")
def test_room(item):
    doc_test = db.collection(u'rooms').document(item)
    doc_test.set({
        'furniture_name': 'TV',
        'size': test00[4]
    })
    return('fin')

@app.get("/change/rooms/{room_id}")
def user_detail(room_id):
    doc_ref = db.collection(u'rooms').document(room_id)
    doc_ref.set({
        'chair': {
            u'furniture_name': test00[0],
            u'position': {test00[1], test00[2]},
            u'rote': test00[3],
            u'size' : test00[4]
        }
    })
    return {"fin"}

@app.get("/rooms/{room_id}")
def user_detail(room_id):
    doc_ref = db.collection(u'rooms').document(room_id)
    doc_ref.set({
        u'furniture_name': test00[0],
        u'position': {test00[1], test00[2]},
        u'rote': test00[3],
        u'size' : test00[4]
    })
    return {"fin"}