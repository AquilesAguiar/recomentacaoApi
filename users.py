from firebase_admin import credentials,firestore

cred = credentials.Certificate("find-her-65a18-352600-firebase-adminsdk-1wb20-f8d77f7bbd.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def getUsersInteresses():
    users_ref = db.collection(u'users')
    docs = users_ref.stream()
    users = dict()
    for doc in docs:
        users[doc.id] = doc.to_dict()["interesses"]
    return users

def getUsers():
    users_ref = db.collection(u'users')
    docs = users_ref.stream()
    users = dict()
    for doc in docs:
        users[doc.id] = doc.to_dict()
    return users