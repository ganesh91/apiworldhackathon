	


client = None
db = None
collection = None

def setInitialMongoParams():
	global client
	global db 
	global collection
	#client = MongoClient("mongodb://admin1:admin@ds149124.mlab.com:49124/apiworldlocodb")
	client = MongoClient("mongodb://admin1:admin@ds149144.mlab.com:49144/apiworldhackathon1")
	db = client['apiworldhackathon1']
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
	