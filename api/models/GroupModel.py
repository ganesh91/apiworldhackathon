from ..models.MongoConnector import *
import json

class Group(object):
	"""docstring for Group"""
	def __init__(self,grpType='usergroup',jsonstr=None):
		super(Group, self).__init__()
		self.group={}
		self.group['id']={'id':None}
		self.groups['group']=[]
		self.groups['type']={'id':'group','groupType':grpType}
		if jsonstr:
			self.group = json.loads(jsonstr)


	def getGroups(self):
		return self.groups['type']['type']

	def addToGroups(self,_grp):
		self.groups['group'].append(_grp)

	def getGroupType(self):
		self.groups['type']['type']

	def setGroupType(self,_type):
		self.groups['id']['id']=_type

	def getJson(self):
		return json.dumps(self.groups)

	def getDict(self):
		return self.groups

	def setDict(self,grp):
		self.groups=_grp
	
