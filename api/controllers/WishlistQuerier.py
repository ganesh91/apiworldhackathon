from ..models.GroupModel import Group
from ..controllers.WalmartAPIQuerier import WalmartAPIQuerier
from ..controllers.GoodznerQuerier import GoodznerAPIQuerier

class WishListQuerier():
	def __init__(self):
		self.walmart=WalmartAPIQuerier()
		self.goodzner=GoodznerAPIQuerier()

	def queryWishlist(self,group,geo):
		result=[]
		lat,lon=geo
		for grp in group.getGroups():
			grpid,grpname=grp
			query_response=self.goodzner.getSearchItem(grpname,geo)
			query_response_wmart_geo=self.walmart.getNearestWalmart(geo)
			query_response_wmart=self.walmart.searchItem(grpname)

			print(query_response_wmart_geo,query_response_wmart)

			for store in query_response['stores']:
				topresult={}
				topresult['address']=",".join([store['locations'][0]['address'],store['locations'][0]['city'],store['locations'][0]['state'],store['locations'][0]['zipcode']])
				topresult['name']=store['name']
				topresult['geo']=",".join([str(store['locations'][0]['lat']),str(store['locations'][0]['lng'])])
				topresult['image']=store['products'][0]['image']
				topresult['price']=store['products'][0]['price']
				topresult['original_price']=store['products'][0]['original_price']
				topresult['product']=store['products'][0]['title']
				result.append(topresult)
		return result

if __name__ == '__main__':
	group = Group()
	gp={'group':[('101','iphone'),('102','denim jeans')],
		'type':{'id':'group','groupType':'wishlist'},
		}
	gp['id']={'id':hash(str(gp))}
	group.setDict(gp)
	wq=WishListQuerier()
	wq.queryWishlist(group,('37.4066001','-122.1451782'))







