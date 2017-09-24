from api.models.MongoActions import MongoManager
from api.models.MongoConnector import *
from api.models.GroupModel import Group

group = Group()
gp={'group':[('101','apple iphone 7 plus'),('102','denim jeans')],
	'type':{'id':'group','groupType':'wishlist'},
	}
gp['id']={'id':hash(str(gp))}
group.setDict(gp)

setInitialMongoParams()
print(getMongoDB(),getMongoDB().collection_names())
api=MongoManager(getCollection())
#api.insertOrUpdate(group.getDict())
print(api.getDocs([{'id.id':1931146094557796051}]))

