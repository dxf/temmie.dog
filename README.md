# temmie.dog
haha temmie go bork bork bork bork bork bork bork bork bork bork bork bork bork
## how to run it
- install python (i use 3.8.5)
- install jinja2, fastapi, aiofiles, uvicorn and pymongo
- set up your own mongodb database and collection
- set credentials and other variables in a file called config.py, use the sample-config.py file for example
- populate your images folder and insert the files using a database schema of basically {'filename': 123.png, 'source': 'insta'} but change source to insta or lilytwi i guess, that field doesn't do much for now
- uvicorn website:app --reload
- profit???
## boring to-do
- add.py script
- gather more temmies (personally, you all can't see the stash)
- deploy