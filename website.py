from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from config import *

from datetime import datetime

import pymongo

client = pymongo.MongoClient(mongodb_address)
db = client[mongodb_db]
collection = db['bork']

app = FastAPI()
templates = Jinja2Templates(directory="pages")
app.mount('/static', StaticFiles(directory="static"),name="static")


@app.get("/bork/image")
def read_item():
    dog = list(collection.aggregate([{"$sample": {"size": 1}}]))
    return FileResponse(content+dog[0]["filename"])

@app.get("/bork/json")
def read_item():
    dog = list(collection.aggregate([{"$sample": {"size": 1}}]))
    return({"url":main+content+dog[0]["filename"],"source":dog[0]["source"]})

@app.get("/api/")
def read_item(request: Request):
    return templates.TemplateResponse("api.html", {"request": request})

@app.get("/")
def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})