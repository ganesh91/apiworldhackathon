import json
import requests

class WalmartAPIQuerier:
	def __init__(self):
		self.key="?apiKey=dfjqqh4d8gcsg2uat4q77gch"
		self.urlhead="http://api.walmartlabs.com/v1"

	def createQueryLink(self,search,params):
		linkbuilder = self.urlhead+'{0}'+ self.key
		linkbuilder = linkbuilder.format(search)
		paramstr="&".join([i[0]+'='+i[1] for i in params])
		finalcallable=linkbuilder+'&'+paramstr
		print(finalcallable)
		return finalcallable

	def getNearestWalmart(self,geo):
		nearestWalmart=None
		lat,lon=geo
		params=[('lat',lat),('lon',lon)]
		response=requests.get(self.createQueryLink('/stores',params))
		if response.status_code==200:
			parse_listing=json.loads(response.text)
			nearestWalmart=parse_listing[0]
		return nearestWalmart

	def searchItem(self,query):
		searchresults=[]
		params=[('query',query)]
		response=requests.get(self.createQueryLink('/search',params))
		if response.status_code==200:
			parse_listing=json.loads(response.text)
			searchresults=parse_listing
		return parse_listing

if __name__ == '__main__':
	api=WalmartAPIQuerier()
	print(api.getNearestWalmart(('37.4108677','-122.1462082')))
	print(api.searchItem('ipod'))


