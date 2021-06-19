import builtins
from os import curdir
from weakref import ProxyTypes
import mysql.connector
import databaseconfig as cfg

mydb = mysql.connector.connect(
    host="localhost",
    user=cfg.mysql["user"],
    password=cfg.mysql["passwd"],
    auth_plugin="mysql_native_password"
)

cursor = mydb.cursor(buffered=True)
try :
    cursor.execute("USE private_diary")
except mysql.connector.Error as err :
    print("Connection failed : {}".format(err))

def makeRequest(request) :
    try :
        cursor.execute(request)
        return cursor
    except mysql.connector.Error as err :
        print("{}".format(err))
        return False