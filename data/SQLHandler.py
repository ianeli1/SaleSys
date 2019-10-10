import sqlite3
dbconn = sqlite3.connect("users.db")
db = dbconn.cursor()

admin_pass = "123"

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
        users = db.execute("SELECT * FROM users WHERE email = ?;",self.email)
        user = user.fetchone()
        if get_hash(user) == self.hash:
            self.id = get_id(user)
            self.name = get_name(user)
            return True
        else:
            self.id = -1
            self.name = "Incorrect Login"
            return False
            # TODO: log this

    def register(self, name, email, hash):
        try:
            db.execute("INSERT INTO users (name,email,hash) VALUES (?,?,?);",[name,email,hash])
        except sqlite3.Error as e:
            # TODO: Log this failed attempt
