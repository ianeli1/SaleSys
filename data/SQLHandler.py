import sqlite3
from logger import action, debug, critical


admin_pass = "123"

def SQLdo(command,args=[]): #executes a command and instantly saves the changes
    dbconn = sqlite3.connect("data/data.db",check_same_thread=False)
    db = dbconn.cursor()
    result = db.execute(command,args)
    dbconn.commit()
    db.close()
    return result


def get_hash(user_object):
    return user_object[3]

def get_email(user_object):
    return user_object[2]

def get_name(user_object):
    return user_object[1]

def get_id(user_object):
    return user_object[0]

# TODO: implement a logging system

class User:
    def __init__(self,email,hash):
        self.email = email
        self.hash = hash


    def login(self):
        users = SQLdo("SELECT * FROM users WHERE email = ?;",self.email)
        user = user.fetchone()
        if get_hash(user) == self.hash:
            self.id = get_id(user)
            self.name = get_name(user)
            action(self.id, "Logged in succesfully.")
            return True
        else:
            self.id = -1
            self.name = "Incorrect Login"
            action(get_id(user), "Failed to provide the correct credentials.")
            return False


    def register(self, name, email, hash):
        # TODO: check if user already exists, check values correct
        try:
            SQLdo("INSERT INTO users (name,email,hash) VALUES (?,?,?);",[name,email,hash])

        except sqlite3.Error as e:
            debug("SQLHandler.User.register", "Database failed to insert new value into users table.")
            print("SQLHandler suffered a critical error!\n", e)
