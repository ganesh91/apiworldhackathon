from api.models.MongoActions import MongoManager
from api.models.MongoConnector import *
from api.models.UserModel import User

user = User()
user.setTrackId("ec3a38ee-0ceb-4e4f-9a70-2a1eabe1f047")
user.setID("user1")
user.addToGroups(['1931146094557796051'])
setInitialMongoParams()
api=MongoManager(getCollection())
#api.insertOrUpdate(user.getDict())
print(api.getDocs([{'id.id':'user1'}]))

