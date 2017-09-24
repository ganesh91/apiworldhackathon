from flask import Flask,render_template
from api.models.MongoConnector import *
from api.controllers.WishlistQuerier import WishListQuerier
from api.models.MongoActions import MongoManager

app = Flask(__name__)
setInitialMongoParams()
api=MongoManager(getCollection())
wlq=WishListQuerier()


@app.route('/<user>/<int:group>')
def show_entries(user,group):
	groups=api.getDocs([{'id.id':group}])
	print(groups)
	obj=wlq.queryWishlist(groups[0],('37.4066001','-122.1451782'))
	#listBuilder='<li data-target="#myCarousel" data-slide-to="{0}"></li>\n'
	#listBuilder1='<div class="carousel-item"><img src="{0}" alt="{1}"><div class="carousel-caption d-none d-md-block"><h3><a href="{5}">{2}</a></h3><p>price {3}</p><p>{4}</p><p></div></div>\n'
	x1='<tr><td>{0}</td></tr><tr><td>{1}</td></tr><tr><td>{2}</td></tr><tr><td>{3}</td></tr><tr><td>{4}</td></tr><tr><td><a href="{5}">{1}</td></tr>'
	c1=""
	c2=""
	for en,i in enumerate(obj):
		# c1+=listBuilder.format(en)
		c1+=listBuilder1.format(i['image'],i['product'],i['product'],i['price'],i['address'],i['url'])
	return render_template('carousel.html', ht=c1)

if __name__ == "__main__":
    app.debug=True
    app.run()
