from ..models.MongoActions import MongoManager
from ..models.UserModel import User

import json

class UserControllers(object):
	"""docstring for UserControllers"""

	def __init__(self, conn):
		super(UserControllers, self).__init__()
		self.mongomanager=MongoManager(conn)

	def createUser(self,args):
		hmap=json.loads(args)
		new_user=User()
		if 'trackid' in hmap:
			new_user.setTrackId(hmap['trackid'])
		if ''



