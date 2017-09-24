from pymongo import MongoClient	


client = None
db = None
collection = None

def setInitialMongoParams():
	global client
	global db 
	global collection
	#client = MongoClient("mongodb://admin1:admin@ds149124.mlab.com:49124/apiworldlocodb")
	#client = MongoClient("mongodb://admin1:admin@ds149144.mlab.com:49144/apiworldhackathon1")
	client = MongoClient("mongodb://127.0.0.1:27017")
	db = client['apiworldhackathon']
	collection = db['apiworldlocodb']

def getMongoClient():
	global client
	return client

def getMongoDB():
	global db
	return db

def getCollection():
	global collection
	return collection
	