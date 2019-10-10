# allows the online service to report every action an user makes and saves it to a local disk
# also allows the automatic reporting of errors
#
from datetime import datetime
action_file = "action.log" #registers every user's action
debug_file = "debug.log" #registers debug messages and errors.



def getTimestamp(): #returns a correctly formatted timestamp
    currTime = datetime.now()
    return "(" + str(currTime.day) + "/" + str(currTime.month) + "/" + str(currTime.year) + " " + str(currTime.hour) + ":" + str(currTime.minute) + ":" + str(currTime.second) + ")"

def log(file, message = "UnknownMessage"):
    logFile = open(file, 'a')
    logFile.write(getTimestamp() + " > " + message + ";\n")
    logFile.close()

def action(usrId = "UnknownUsrId", message = "No message reported", pr = False):
    log(action_file, "[" + str(usrId) + "] > " + message)
    if pr:
        print("[" + str(usrId) + "] > " + message)

def debug(location = "NoLocationReported", message = "No message reported"):
    log(debug_file, "[" + location + "] > " + message)

def critical(location, message, allDataKnown):
    err = "!!!CRITICAL-ERROR-REPORTED-AUTOMATICALLY ["+ location +"] > " + message + "\n > " + str(allDataKnown)
    log(debug_file, err)
    print("======================================")
    print(err)
    print("======================================")
