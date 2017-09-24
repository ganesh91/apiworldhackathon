from api.models.GroupModel import Group
from api.controllers.WishlistQuerier import WishListQuerier
group = Group()
gp={'group':[('101','apple iphone 7 plus'),('102','denim jeans')],
	'type':{'id':'group','groupType':'wishlist'},
	}
gp['id']={'id':hash(str(gp))}
group.setDict(gp)
wq=WishListQuerier()
for i in wq.queryWishlist(group,('37.4066001','-122.1451782')):
	print(i)