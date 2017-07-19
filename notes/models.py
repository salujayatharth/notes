from database import db
from bson.objectid import ObjectId

def save_cookie(id_cookie):
    if not isinstance(id_cookie, str):
        return None

    data = {
        "id_cookie": id_cookie
    }
    user_id = db.cookies.insert_one(data).inserted_id

    return user_id

def create_user(user_id):
    if not isinstance(user_id, str):
        return None
    
    data = {
        "_id": ObjectId(user_id)
    }

    user_id = db.users.insert_one(data).inserted_id
    return user_id

def check_user(id_cookie):
    if not isinstance(id_cookie, str):
        return None

    result = db.cookies.find_one({"id_cookie" : id_cookie})
    
    if not result:
        return None
    return result["_id"]

def save_note(user_id, title, note):
    if not isinstance(user_id, str):
        return False
    if not isinstance(note, str):
        return False
    if not isinstance(title, str):
        return False

    data = {
        "_id": ObjectId(user_id),
        "title" : title,
        "note": note
    }
    note_id = db.notes.insert_one(data).inserted_id
    
    return bool(note_id)

def get_notes(user_id):
    if not isinstance(user_id, str):
        return None

    notes = db.notes.find({"_id" : ObjectId(user_id)})

    if notes.count() == 0:
        return None
    return notes
