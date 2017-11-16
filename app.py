import urllib2
import requests
import json
from flask import Flask, session, url_for, redirect, render_template, request
import os

#App instantiation
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/redirecting")
def redirecting():
    if (request.args["choice"] == "space"):
        return redirect("/space")
    else:
        return redirect("/recipes_search")  

@app.route("/recipes_search")
def food():
    return render_template("recipe_search.html") 

@app.route("/results")
def display_food():
    #Grabs ingredient keywords that the user entered

    keywords = request.args["ingredients"]

    #Accesses the site through specific keywords for the search query 
    site= "http://food2fork.com/api/search?key=95e985762f234c8784ac3d8c57a1f3dd&q="
    site+=keywords
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site,headers=hdr)
    uResp = urllib2.urlopen(req)

    #Grabbing information 
    site_content = uResp.read()

    #Turning grabebd information into a dictionary 
    d = json.loads(site_content)

    #Removing one unnecessary key from the dictionary 
    d.pop("count")

    return render_template("results.html", d = d["recipes"]) 

if __name__ == "__main__":
    app.debug = True

app.run()
