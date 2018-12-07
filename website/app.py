from flask import Flask
from flask import render_template
import pymongo
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
#DBS_NAME = 'donorschoosee'
#COLLECTION_NAME = 'projects'
DBS_NAME = 'twitterdb'
COLLECTION_NAME = 'AirPods'

DBS_NAME_TWO = 'twitterdb'
COLLECTION_NAME_TWO = 'iPhone'

DBS_NAME_THREE = 'twitterdb'
COLLECTION_NAME_THREE = 'iPad'

DBS_NAME_FOUR = 'twitterdb'
COLLECTION_NAME_FOUR = 'Watch'

FIELDS = {'school_state': True, 'resource_type': True, 'funding_status': True, 'date_posted': True, 'total_donations': True}#, '_id': False}

json_projectss = []

connection = pymongo.MongoClient("mongodb+srv://yh2866:Aa123456@cluster0-5mcg4.mongodb.net/tttest?retryWrites=true")
collection = connection[DBS_NAME][COLLECTION_NAME]

projects = collection.find(projection=FIELDS, limit=100000)
# projects = collection.find(projection=FIELDS)
json_projects = []
for project in projects:
    json_projects.append(project)
connection.close()

####################  Add for the second database
connection = pymongo.MongoClient("mongodb+srv://yh2866:Aa123456@cluster0-5mcg4.mongodb.net/tttest?retryWrites=true")
collection = connection[DBS_NAME_TWO][COLLECTION_NAME_TWO]

projects = collection.find(projection=FIELDS, limit=100000)
for project in projects:
    json_projects.append(project)
connection.close()
#####################

#####################
connection = pymongo.MongoClient("mongodb+srv://yh2866:Aa123456@cluster0-5mcg4.mongodb.net/tttest?retryWrites=true")
collection = connection[DBS_NAME_THREE][COLLECTION_NAME_THREE]

projects = collection.find(projection=FIELDS, limit=100000)
for project in projects:
    json_projects.append(project)
connection.close()
#######################

#####################
connection = pymongo.MongoClient("mongodb+srv://yh2866:Aa123456@cluster0-5mcg4.mongodb.net/tttest?retryWrites=true")
collection = connection[DBS_NAME_FOUR][COLLECTION_NAME_FOUR]

projects = collection.find(projection=FIELDS, limit=100000)
for project in projects:
    json_projects.append(project)
connection.close()
#######################

json_projectss = json.dumps(json_projects, default=json_util.default)

@app.route("/")
def index():
    return render_template("main.html")


@app.route("/lda")
def lda():
    return render_template("lda.html")

@app.route("/map")
def map():
    return render_template("index.html")


@app.route("/donorschoose/projects")
def donorschoose_projects():
    #connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    #collection = connection[DBS_NAME][COLLECTION_NAME]

    

    
    
    
    return json_projectss

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)