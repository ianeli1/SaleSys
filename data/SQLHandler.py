import sqlite3
from logger import action, debug, critical


admin_pass = "123" # TODO: implement

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
        self.name = ""
        self.email = str(email)
        self.hash = str(hash)
        self.id = 0


    def login(self):
        users = SQLdo("SELECT * FROM users WHERE email = ?;",[self.email])
        if len(user):
            user = users[0]
            if get_hash(user) == self.hash:
                self.id = get_id(user)
                self.name = get_name(user)
                action(self.id, "Logged in succesfully.")
                return True
            else:
                action(get_id(user), "Failed to provide the correct credentials.")
                return False
        else:
            action(self.email, "User not found")
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

class Item:
    def __init__(self, name):
        self.name = name
        self.id = 0
        self.comment = ""
        self.amount = -9999
        self.price = -9999

    def create(self):
        try:
            SQLdo("INSERT INTO inv (name,comment,amount,price) VALUES (?,?,?,?);",[self.name,self.comment,self.amount,self.price])
            self.fetch()
            return True
        except sqlite3.Error as e:
            debug("SQLHandler.User.register", "Database failed to insert new value into users table.")
            print("SQLHandler suffered a critical error!\n", e)
            return False

    def fetch(self):
        items = SQLdo("SELECT * FROM inv WHERE name = ?;",[self.name])
        if len(items):
            item = items[0]
            self.id = item[0]
            self.comment = item[2]
            self.amount = item[3]
            self.price = item[4]
            return True
        else:
            return False

    def push(self):
        # TODO: push values to db
        if id != 0:
            try:
                SQLdo("UPDATE inv SET name = ?, comment = ?, amount = ?, price = ? WHERE itemId = ?",[self.name, self.comment, self.amount, self.price, self.id])
                return True
            except sqlite3.Error as e:
                debug("SQLHandler.Item.push","Couldn't update inv item with id = " + str(self.id))
                print("SQLHandler suffered a critical error!\n",e)
                return False
        else:
            return False

    def change(self, difference):
        if isinstance(difference, int) or isinstance(difference, float):
        self.fetch()
        if difference < 0 and (-1)*difference > self.amount:
            # TODO: report this
            return False


    def setAmount(self,value):
        if isinstance(value, int) or isinstance(value, float):
            self.amount = value
            return True
        else:
            return False

    def getAmount(self):
        self.fetch()
        return self.amount

    def setPrice(self,value):
        self.price = value

    def getPrice(self):
        self.fetch()
        return self.price

    def setComment(self,value):
        if isinstance(value, str):
            self.comment = value
            return True
        else:
            return False

    def getComment(self):
        self.fetch()
        return self.comment

    def setName(self, value):
        if isinstance(value, str):
            self.name = value
            return True
        else:
            return False

    def getName(self):
        return self.name

    def setId(self, value):
        return False #SQL wouldn't like that

    def getId(self):
        return self.id
