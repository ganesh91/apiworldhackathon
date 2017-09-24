from flask import Flask
from api.models.MongoConnector import *
from api.controllers.WishlistQuerier import WishListQuerier

app = Flask(__name__)
setInitialMongoParams()
api=MongoManager(getCollection())
wlq=WishlistQuerier()


@app.route('/<user>/<int:group>')
def show_entries(user,group):
	print(group)
	groups=api.getDocs([{'id.id':group}])
	obj=wq.queryWishlist(group,('37.4066001','-122.1451782'))
	print(obj)

    return render_template('carousel.html', carouselitems1='<hr>',carouselitems2='<hr>')

if __name__ == "__main__":
    app.debug=True
    app.run()
