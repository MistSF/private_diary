from fastapi import APIRouter
from starlette.requests import Request
from function.db import mydb, makeRequest

coachRouter = APIRouter()

@coachRouter.post("/add")
async def addClient(firstname, lastname) :
    """
    Add a new client
    """
    request = "INSERT INTO client (FirstName, LastName) VALUES ('{}', '{}')".format(firstname, lastname)
    makeRequest(request)
    mydb.commit()
    return True

@coachRouter.get("/clients")
async def getList() :
    """
    Get list of clients
    """
    request = "SELECT * FROM client;"
    return makeRequest(request)

@coachRouter.delete("/delClient")
async def delClient(ID) :
    """
    Remove client
    """
    request = "DELETE FROM client WHERE ID = {}".format(ID)
    makeRequest(request)
    mydb.commit()
    return True

@coachRouter.put("/update")
async def updateClient(ID, firstname=None, lastname=None) :
    request = "UPDATE client SET "
    if firstname != None :
        request += "FirstName = '{}'".format(firstname)
        if lastname != None :
            request += ", "
    elif lastname != None :
        request += "LastName = '{}'".format(lastname)
    else :
        return False
    request += "WHERE ID = {}".format(ID)
    makeRequest(request)
    mydb.commit()
    return True

@coachRouter.get("/getCliennt/{id}")
async def getClient(id) :
    request = "SELECT * FROM client WHERE ID = '{}'".format(id)
    return makeRequest(request)