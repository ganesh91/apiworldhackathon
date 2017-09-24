from ..models.MongoConnector import *
import json

class User(object):
	"""docstring for User"""
	def __init__(self,jsonstr=None):
		super(User,self).__init__()
		self.user={}
		self.user['type']={"id":'User'}
		self.user['id']={'id':None,'trackid':None}
		self.user['person_info']={'name':None,'primary_email':None,'phone':None}
		self.user['geo']={'last_seen':None}
		self.user['groups']=[]
		if jsonstr:
			self.user=json.loads(jsonstr)

	def toJson(self):
		return json.dumps(self.user)

	def fromJson(self,jsonstr):
		self.user = json.loads(jsonstr)

	def getID(self):
		return self.user['id']['id']

	def getTrackId(self):
		return self.user['id']['trackid']

	def getLastSeen(self):
		return self.user['geo']['last_seen']

	def setID(self,_id):
		self.user['id']['id']=_id

	def setTrackId(self,_id):
		self.user['id']['trackid']=_id

	def setLastSeen(self,lastseen):
		self.user['geo']['last_seen']=lastseen

	def getDict(self):
		return self.user

	def setDict(self,_dict):
		self.user = _dict

	def getGroups(self):
		return self.user['groups']

	def addToGroups(self,groupids):
		self.user['groups']+=groupids

	def removeGroups(self,groupids):
		self.user.groups=[i for i in self.user['groups'] if i not in groupids]





