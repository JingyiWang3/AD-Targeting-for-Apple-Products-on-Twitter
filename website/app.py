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
DBS_NAME = 'ttest'
COLLECTION_NAME = 'projects'

FIELDS = {'school_state': True, 'resource_type': True, 'funding_status': True, 'date_posted': True, 'total_donations': True}#, '_id': False}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/lda")
def lda():
    return render_template("lda.html")


@app.route("/donorschoose/projects")
def donorschoose_projects():
    #connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    #collection = connection[DBS_NAME][COLLECTION_NAME]
    connection = pymongo.MongoClient("mongodb+srv://yh2866:Aa123456@cluster0-5mcg4.mongodb.net/ttest?retryWrites=true")
    collection = connection[DBS_NAME][COLLECTION_NAME]

    projects = collection.find(projection=FIELDS, limit=10000)
    # projects = collection.find(projection=FIELDS)
    json_projects = []
    # i = 0
    for project in projects:
        # i += 1
        # if (i > 10000):
        #     break
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    
    connection.close()
    return json_projects

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)