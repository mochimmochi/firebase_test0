import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from fastapi import FastAPI

cred = credentials.Certificate(".\\.gitignore\\first-test-2fc42-firebase-adminsdk-2limr-9396562c62.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
app = FastAPI()

# user_detail = {
#   roomid:{
#     chest:{
#       position:[0,0],
#       size:1.0
#       rote:90
#       },
#     chair:{
#       position:[0,0],
#       size:1.0
#       rote:90
#       }
#   }
# }
import numpy as np
import re
a = 'chair&box&TV'
a_list = re.findall('[a-z]+' , a, flags=re.IGNORECASE)
print(a)
print(a_list)
b = '[0,10]&[2,3]&[40, 5]'
b_list = re.findall('[0-9]+', b)
print(b)
print(b_list)
print(type(b_list))
b_int = [int(num) for num in b_list]
b_d = np.array(b_list, dtype = int)
b_dre = b_d.reshape([-1, 2])
print(b_dre.shape[0])
c = '100.00, 10, 0.4'
c_list = re.findall('[0-9]+[.]*[0-9]+', c)
print(c)
print(c_list)
c_d = [float(num) for num in c_list]
print(c_d)
e = '10, 20, 30'
e_list = re.findall('[0-9]+', e)
e_d = [int(num) for num in e_list]
add = 'detail@gmail.com'
d_detail = {
    add :{
        a_list[0]:{
            'position': [b_int[0], b_int[1]],
            'size':c_d[0],
            'rote':e_d[0]
            },
        a_list[1]:{
            'position':[0, 0],
            'size': 1.0,
            'rote': 90
            }
    }
}
print(d_detail)
for i in range(len(a_list)):
    print(i)
    dict = {
            'position': [b_int[i*2], b_int[i*2+1]],
            'size':c_d[i],
            'rote':e_d[i]
            }
    d_detail[add][a_list[i]] = dict
print(d_detail)
d = {'da':{}}
print(type(d))
#print((d_detail['detail@gmail.com']['chair']))
#print(type(d_detail['detail@gmail.com']['box']['size']))

#/chest&chair/[0,0]&[0,0]/[1.0,1.0]/[90,90]

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
    
#{room_id}/{furniture_name}/{position}/{size}/{rote}
    
@app.post("/API")
def display(room_id: str, furniture_name: str, position: str, size: str, rote: str):
    furniture_name_list = re.findall('[a-z]+|[0-9]+' , furniture_name, flags=re.IGNORECASE)
    position_str_list = re.findall('[0-9]+', position)
    position_list = [int(num) for num in position_str_list]
    size_str_list = re.findall('[0-9]+[.]*[0-9]+', size)
    size_list = [float(num) for num in size_str_list]
    rote_str_list = re.findall('[0-9]+', rote)
    rote_list = [int(num) for num in rote_str_list]
    detail={room_id:{}}
    for i in range(len(furniture_name_list)):
        dict = {
            'position': [position_list[i*2], position_list[i*2+1]],
            'size':size_list[i],
            'rote':rote_list[i]
            }
        detail[room_id][furniture_name_list[i]] = dict
    print(detail)
    return(save_detail(detail))
    #return{room_id, furniture_name_list[0], position_list[0], size_list[0], rote_list[0]}
    #return{room_id, furniture_name, position, size, rote, furniture_name_list[0]}

@app.get("/API2")
def display(room_id: str, furniture_name: str, position: str, size: str, rote: str):
    furniture_name_list = re.findall('[a-z]+|[0-9]+' , furniture_name, flags=re.IGNORECASE)
    position_str_list = re.findall('[0-9]+', position)
    position_list = [int(num) for num in position_str_list]
    size_str_list = re.findall('[0-9]+[.]*[0-9]+', size)
    size_list = [float(num) for num in size_str_list]
    rote_str_list = re.findall('[0-9]+', rote)
    rote_list = [int(num) for num in rote_str_list]
    detail={room_id:{}}
    for i in range(len(furniture_name_list)):
        dict = {
            'position': [position_list[i*2], position_list[i*2+1]],
            'size':size_list[i],
            'rote':rote_list[i]
            }
        detail[room_id][furniture_name_list[i]] = dict
    print(detail)
    return(save_detail(detail))


user_detail_test = {
    "detail@gmail.com":{
        "chest":{
            "position": [0, 0],
            "size":1.0,
            "rote":90
            },
        "chair":{
            "position":[0, 0],
            "size":1.0,
            "rote":90
            }
    }
}
# print(user_detail_test['detail@gmail.com'])
# key = user_detail_test.keys()
# print(key)
# print(type(key))
# print(str(key))
# print(type(str(key)))
# key_str = str(key)
# print(key_str)
# print(key_str[12:-3])

@app.get("/save_detail")
def appsave_detail():
    return(save_detail(user_detail_test))

def save(room_id, **user_detail):
    try:
        user_detail_ref = db.collection(u'rooms').document(room_id)
        user_detail_ref.set({
            user_detail['furniture_name']:user_detail
        })
    except Exception as e:
        print(e)
        return False
    else:
        return True
    
def save_to(**user_detail):
    try:
        user_detail_ref = db.collection(u'rooms').document(user_detail['room_id'])
        remove_room_id = user_detail.pop('room_id')
        user_detail_ref.set({
            user_detail['furniture_name']:user_detail
        })
        user_detail['room_id'] = remove_room_id
    except Exception as e:
        print(e)
        return False
    else:
        return True


test02 ={'room_id':'oo', 'furniture_name':'box', 'position':{1, 2}, 'size':20, 'rote':30}
#print(test02)
#, furniture_name: str, position_x: int, position_y: int, size: float, rote: int

@app.get("/test02/{room_id}")
def test02_test(room_id):
    #test03 = {room_id: {furniture_name:{}, furniture_name: {}}}
    return (save(room_id, **test02))

test03 ={'room_id':'test03@gmail.com_1', 'furniture_name':'box', 'position':{1, 2}, 'size':20, 'rote':30}
#print(test03)
@app.get("/test03/{user_detail}")
def test03_test():
    return (save(**user_detail_test))
