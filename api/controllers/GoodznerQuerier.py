import requests
import json

class GoodznerQuerier:
	def __init__(self):
		self.urlhead="https://api.goodzer.com/products/v0.1/search_stores/?query={0}&lat={1}&lng={2}&radius=5&apiKey=2503ff758d0f2dc3cceba62a170a59df"

	def getSearchItem(self,query,geo):
		result=[]
		lat,lon=geo
		pingurl=self.urlhead.format(query,lat,lon)
		response=requests.get(pingurl)
		if response.status_code==200:
			result=response