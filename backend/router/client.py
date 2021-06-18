from sys import implementation
from fastapi import APIRouter
from starlette.requests import Request
from starlette.routing import request_response
from function.db import mydb, makeRequest
from datetime import datetime

clientRouter = APIRouter()

@clientRouter.get("/alltext")
async def getAllText(id_client) :
    request = "SELECT * FROM texte WHERE ID_client = {}".format(id_client)
    return makeRequest(request)

@clientRouter.get("/text/{id}")
async def getText(id_client, id) :
    request = "SELECT * FROM texte WHERE ID = {} AND ID_client = {}".format(id, id_client)
    return makeRequest(request)

@clientRouter.post("/newText")
async def newText(id_client, text) :
    now = datetime.now()
    request = "INSERT INTO texte (Content, Post_Date, Last_Update, Sentiment, ID_Client) VALUES (\"{}\", '{}', '{}', '{}', '{}')".format(
        text,
        now,
        now,
        "",
        id_client
    )
    makeRequest(request)
    mydb.commit()
    return True

@clientRouter.put("/updateText/{id}")
async def updateText(id_client, id, text):
    request = "UPDATE texte SET Content = '{}', Last_Update = {} WHERE ID = '{}' AND ID_client = \"{}\"".format(
        text, 
        datetime.now(), 
        id, 
        id_client)
    makeRequest(request)
    mydb.commit()
    return  True