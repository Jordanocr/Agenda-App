import database as db

def getUsers():
    """ Calls the database interaction function to fetch user names. """
    users = db.fetchUsers() # Not working yet

def saveAppointment(data:dict,edit=False):
    """ Calls the database interaction function to save or rewrite user data"""
    try:
        if edit:
            db.editAppointment(data)
        else:
            db.createAppointment(data)
    except Exception:
        raise ConnectionRefusedError