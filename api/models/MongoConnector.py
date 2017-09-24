from pymongo import MongoClient


client = None
db = None
collection = None

def setInitialMongoParams():
	global client
	global db 
	global collection
	client = MongoClient("mongodb://admin:admin@ds149124.mlab.com:49124")
	db = client['apiworldlocodb']
	collection = db['locogroups']

def getMongoClient():
	global client
	return client

def getMongoDB():
	global db
	return db

def getCollection():
	global collection
	return collection
	