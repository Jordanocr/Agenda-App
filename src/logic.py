import database as db

def saveAppointment(data:dict,edit=False):
    """ Calls the database interaction function to save or rewrite user data"""
    if edit:
        db.editAppointment(data)
    else:
        db.createAppointment(data)