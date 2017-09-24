from flask import Flask,render_template
from api.models.MongoConnector import *
from api.controllers.WishlistQuerier import WishListQuerier
from api.models.MongoActions import MongoManager
import requests
import json

app = Flask(__name__)
setInitialMongoParams()
api=MongoManager(getCollection())
wlq=WishListQuerier()


@app.route('/<user>/<group>')
def show_entries(user,group):
	uri='https://api.hypertrack.com/api/v1/users/{0}'
	print(uri.format(user))
	x=requests.get(uri.format(user),headers={'Authorization':'token sk_test_23ef034fbd8c385fdd723419d39a535df94ad042','Content-Type':'application/json'},data={})
	#return x.text
	q= ",".join([json.loads(x.text)['name'],str(json.loads(x.text)['last_location']['geojson']['coordinates'][1]),str(json.loads(x.text)['last_location']['geojson']['coordinates'][0])])
	q=q.split(",")
	groups=api.getDocs([{'id.id':group}])
	x1='<tr><td><img src="{0}"></img></td><td>{1}</td><<td>{2}</td><td>{3}</td><td>{4}</td><td><a href="{5}">{1}</td></tr>'
	c1=""
	c2=""
	c1+='<h2> Welcome {0}, Your Last known lat,lon is {1}{2}</h2><br>'.format(q[0],q[1],q[2])
	for group in groups:
		print("sdsd",group)
		obj=wlq.queryWishlist(group,(q[-2],q[-1]))
		#listBuilder='<li data-target="#myCarousel" data-slide-to="{0}"></li>\n'
		#listBuilder1='<div class="carousel-item"><img src="{0}" alt="{1}"><div class="carousel-caption d-none d-md-block"><h3><a href="{5}">{2}</a></h3><p>price {3}</p><p>{4}</p><p></div></div>\n'
		for en,i in enumerate(obj):
			# c1+=listBuilder.format(en)
			c1+=x1.format(i['image'],i['name'],i['product'],i['price'],i['address'],i['url'])
	return render_template('carousel.html', ht=c1)


@app.route("/hypertrack/<user>")
def showusers(user):
	uri='https://api.hypertrack.com/api/v1/users/{0}'
	print(uri.format(user))
	x=requests.get(uri.format(user),headers={'Authorization':'token sk_test_23ef034fbd8c385fdd723419d39a535df94ad042','Content-Type':'application/json'},data={})
	#return x.text
	return ",".join([json.loads(x.text)['name'],str(json.loads(x.text)['last_location']['geojson']['coordinates'][1]),str(json.loads(x.text)['last_location']['geojson']['coordinates'][0])])

if __name__ == "__main__":
    app.debug=True
    app.run()
