from api.models.GroupModel import Group
from api.controllers.WishlistQuerier import WishListQuerier
group = Group()
gp={'group':[('101','iphone'),('102','denim jeans')],
	'type':{'id':'group','groupType':'wishlist'},
	}
gp['id']={'id':hash(str(gp))}
group.setDict(gp)
wq=WishListQuerier()
wq.queryWishlist(group,('37.4066001','-122.1451782'))