import pymongo
from pymongo import MongoClient
from sanic import Sanic, response
from sanic.response import json 


app = Sanic("Test")

cluster = pymongo.MongoClient("mongodb://mongodb:27017/")

db = cluster["Docker"]
collection = db["Docker1"]


@app.route("/") 
async def index(request):
    return json({'Welcome to my first': 'app'})

@app.route("/json", methods=['POST'])
def post_json(request):
    post = collection.insert_one(request.json).inserted_id

    return json({ "received": True, "massage": str(post)})

@app.route("/test3", methods=["GET"])
def get_json(response):
    get=list(collection.find({},{ "_id": 0, "content": 1, "title": 1 }).limit(10))
    return json({"Content":str(get)})


    
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)