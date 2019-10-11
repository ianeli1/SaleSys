import sqlite3
from logger import action, debug, critical


admin_pass = "123"

def SQLdo(command,args=[]): #executes a command and instantly saves the changes
    dbconn = sqlite3.connect("data/data.db",check_same_thread=False)
    db = dbconn.cursor()
    result = db.execute(command,args).fetchall()
    db.close()
    dbconn.commit()
    dbconn.close()

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
        self.email = str(email)
        self.hash = str(hash)
        self.id = 0


    def login(self):
        users = SQLdo("SELECT * FROM users WHERE email = ?;",[self.email])
        user = users[0]
        if get_hash(user) == self.hash:
            self.id = get_id(user)
            self.name = get_name(user)
            action(self.id, "Logged in succesfully.")
            return True
        else:
            self.id = 0
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

    def get_id(self):
        if self.id != 0:
            return self.id
        elif self.login():
            return self.id
        else:
            return "Login failed."

    def get_name(self):
        if self.id != 0:
            return self.name
        elif self.login():
            return self.name
        else:
            return "Login failed."

    def get_email(self):
        if self.id != 0:
            return self.email
        elif self.login():
            return self.email
        else:
            return "Login failed."

    def get_hash(self):
        if self.id != 0:
            return self.hash
        elif self.login():
            return self.hash
        else:
            return "Login failed."
