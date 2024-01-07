from flask import Flask, render_template
from webscraping import getNext13Games
from competition import *
from stryktipset import *
  
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__, template_folder='templates', static_folder='statics')
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.


def hello_world():
    myCoupon= Coupon()
    myPremierLeague = Competition(urlPremierLeague)
    myChampionship = Competition(urlChampionship)
    getNext13Games(myCoupon, myPremierLeague, myChampionship)
    return render_template('index.html', coupon_rows=myCoupon.getRows())
  
# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug="true")   


