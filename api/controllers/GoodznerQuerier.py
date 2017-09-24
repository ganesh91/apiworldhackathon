import requests
import json

class GoodznerAPIQuerier:
	def __init__(self):
		self.urlhead="https://api.goodzer.com/products/v0.1/search_stores/?query={0}&lat={1}&lng={2}&radius=5&apiKey=2503ff758d0f2dc3cceba62a170a59df"

	def getSearchItem(self,query,geo):
		result=[]
		lat,lon=geo
		pingurl=self.urlhead.format(query,lat,lon)
		response=requests.get(pingurl)
		if response.status_code==200:
			result=json.loads(response.text)
		return result

if __name__ == '__main__':
	api=GoodznerQuerier()
	print(api.getSearchItem("ipod music player",('37.4108677','-122.1462082')))