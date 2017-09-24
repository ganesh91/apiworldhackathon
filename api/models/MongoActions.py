from ..models.MongoConnector import *
from bson.objectid import ObjectId
from ..models.UserModel import User
from ..models.GroupModel import Group


class MongoManager(object):
	"""docstring for MongoManager"""
	def __init__(self, conn):
		super(MongoManager, self).__init__()
		self.conn = conn

	def insertOrUpdate(self,jsonobj):
			if "_id" in jsonobj:
				self.conn.replace_one({"_id":ObjectId(jsonobj['_id'])},jsonobj,True)
			else:
				self.conn.insert_one(jsonobj)

	def getId(self,id):
		return self.toModel(self.conn.find_one({"_id":ObjectId(id)}))

	def getDocs(self,querys):
		result=[]
		for query in querys:
			result+=[i for i in self.conn.find(query)]
		result_models = [self.toModel(i) for i in result]
		return result_models

	def toModel(self,result):
		new_object=None
		print(result)
		if "type" in result:
			if result['type']['id'] == 'User':
				new_object = User()
				new_object.setDict(result)
			if result['type']['id'] == 'group':
				new_object = Group()
				new_object.setDict(result)
		return new_object

	def toModels(self,resultset):
		result=[]
		for _row in resultset:
			result.append(self.toModel(_row))
		return result



