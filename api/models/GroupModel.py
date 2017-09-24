from ..models.MongoConnector import *
import json

class Group(object):
	"""docstring for Group"""
	def __init__(self,grpType='usergroup',jsonstr=None):
		super(Group, self).__init__()
		groups={}
		groups['id']={'id':None}
		groups['group']=[]
		groups['type']={'id':'group','groupType':grpType}
		if jsonstr:
			groups = json.loads(jsonstr)
		self.groups=groups


	def getGroups(self):
		return self.groups['group']

	def addToGroups(self,_grp):
		self.groups['group'].append(_grp)

	def getGroupType(self):
		self.groups['type']['groupType']

	def setGroupType(self,_type):
		self.groups['type']['groupType']=_type

	def getJson(self):
		return json.dumps(self.groups)

	def getDict(self):
		return self.groups

	def setDict(self,_grp):
		self.groups=_grp
	
