import sqlite3

dbPath = "src/data/database.db"
foreignKey = "PRAGMA foreign_keys = ON;"

def createSchema():
    """ Creates the database if it doesn't exist. """
    # ====== Reads the schema.sql file ======
    scriptPath = "src/data/schema.sql"
    with open(scriptPath,"r",encoding="utf-8") as schema:
        script = schema.read()
    
    # ====== Creates the database ======
    with sqlite3.connect(dbPath) as connection:
        connection.executescript(script)
        connection.commit()

def contextManager(script):
    """ Manages the execution of scripts on the database. """
    # ====== Creates the context structure and executes the given script ======
    with sqlite3.connect(dbPath) as connection:
        cursor = connection.cursor()
        cursor.execute(foreignKey)
        cursor.executescript(script)
        connection.commit()
        return cursor.fetchall()

def fetchUsers():
    """ Fetch the name of all users. """
    script = """SELECT name FROM users """
    contextManager(script)

createSchema()