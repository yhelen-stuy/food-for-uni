from flask import Flask, session, url_for, redirect, render_template, request
import urllib2
import requests
import json
import api

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

@app.route("/recipes")
def display_food(): #Grabs ingredient keywords that the user entered

    '''
    keywords = request.args["ingredients"]

    sort = request.args["sort"]

    '''
    #Accesses the site through specific keywords for the search query 

    site= "http://food2fork.com/api/search?key=95e985762f234c8784ac3d8c57a1f3dd&"

    #ADD IN HOW YOU SORT
    sort_link = "sort=h&"
    site += sort_link
    add = "q="
    site += add
    site+=keywords

    print site

    '''
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site,headers=hdr)
    uResp = urllib2.urlopen(req)

    #Grabbing information
    site_content = uResp.read()

    #Turning grabebd information into a dictionary
    d = json.loads(site_content)

    #Removing one unnecessary key from the dictionary
    d.pop("count")
    '''

    return render_template("recipe_results.html", d = d["recipes"])

@app.route("/restaurant_search", methods=["GET"])
def rest_search():
    return render_template("restaurant_search.html")

@app.route("/restaurant_results", methods=["GET"])
def restaurant_results():
    args = request.args
    if args['cuisines']:
        cuisines = []
    else:
        cuisines = args['cuisines'].split(',')
    sort = args['sort']
    order = args['order']
    rests = api.restaurant_search(args['query'],
                                    args['location'],
                                    args['radius'],
                                    args['max_amt'],
                                    cuisines,
                                    args['sort'],
                                    args['order'])
    # if not (q or rad or max_amt or not cuisines.empty()):
    #     if loc:
    #         return redirect(url_for('restaurant_rec')) # send location info
    #     else:
    #         return redirect(url_for('restaurant_rec'))
    return render_template("restaurant_results.html",
            rests = rests['restaurants'])

if __name__ == "__main__":
    app.debug = True
    app.run()
