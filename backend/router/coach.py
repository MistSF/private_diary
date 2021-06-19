from fastapi import APIRouter
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
    return makeRequest(request).fetchall()

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
async def updateClient(ID, firstname, lastname) :
    print(ID, firstname, lastname)
    request = "UPDATE client SET FirstName = '{}', LastName = '{}'  WHERE ID = '{}'".format(firstname, lastname, ID)
    makeRequest(request)
    mydb.commit()
    return True

@coachRouter.get("/getCliennt/{id}")
async def getClient(id) :
    request = "SELECT * FROM client WHERE ID = '{}'".format(id)
    return makeRequest(request).fetchall()