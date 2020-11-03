# import.py - this script is used for batch imports of images. adding individual images should be done via the add.py script

# import libs
import pymongo
from config import *
from os import listdir,rename
# connect to database
client = pymongo.MongoClient(mongodb_address_admin)
db = client[mongodb_db]
collection = db['bork']
# define where you keep a local mirror of your images directory here
dire = "/Users/daf/temmie-content/images/"
# recursively list through your image directory, adding each image to the database
for i in listdir(dire):
    if i[0] == "i":
        source = "insta"
    elif i[0] == "t":
        source = "lilytwi"
    image = {
        "filename": i,
        "source": source
    }
    collection.insert_one(image)