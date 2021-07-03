from typing_extensions import runtime
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)
#Use flask mongo to set up connection between python and mongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#Define the route for the html page
@app.route("/")
def index():
    mars= mongo.db.mars.find_one()
    return render_template("index2.html", mars=mars)

#Set up the scraping route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)


#Run flask
if __name__ == "__main__":
   app.debug = True  
   app.run()
