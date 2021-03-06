from flask import Flask, session, url_for, redirect, render_template, request, flash
import urllib2
import requests
import json
import os
import api

#App instantiation
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/redirecting")


@app.route("/recipes_search")
def food():
    return render_template("recipe_search.html")

@app.route("/recipes")
def search(): #Grabs ingredient keywords that the user entered
    site= "http://food2fork.com/api/search?key=95e985762f234c8784ac3d8c57a1f3dd&"
    hdr = {'User-Agent': 'Mozilla/5.0'}

    #Accesses the site through specific keywords for the search query
    global ingredients 
    ingredients = request.args["ingredients"].lower()
    ingredients = ingredients.replace(" ", "") 

    global ing_to_avoid
    ing_to_avoid = request.args["ing_to_avoid"].lower().split(",")
    print ing_to_avoid

    sort_link = "sort="
    sort_link += request.args["sort"] 
    site += sort_link

    ing_link = "&q="
    ing_link += ingredients 
    site+=ing_link

    req = urllib2.Request(site,headers=hdr)
    uResp = urllib2.urlopen(req)

    #Grabbing information
    site_content = uResp.read()

    #Turning grabebd information into a dictionary
    global d 
    d = json.loads(site_content)

    if (d['count'] == 0):
        #print("no results")
        site = "http://food2fork.com/api/search?key=95e985762f234c8784ac3d8c57a1f3dd&"
        if (sort_link == "sort=r"):
            message = "Oops, looks like there were no hightest rating recipes with the entered ingredients. Check to see the trendy recipes instead?"
            sort_link = "sort=t"
        else:
            message = "Oops, looks like there were no trendy recipes with the entered ingredients. Check to see the highest rated recipes instead?"
            sort_link = "sort=r"

        site += sort_link 
        site += ing_link
        #print ("new site:" + site) 
        req = urllib2.Request(site,headers=hdr)
        uResp = urllib2.urlopen(req)

        #Grabbing information
        site_content = uResp.read()

        #Turning grabebd information into a dictionary 
        d = json.loads(site_content)

        return render_template("redirect.html", message = message)

    return redirect("/recipes_results") 

@app.route("/recipes_results")
def recipes_results():
    global d
    for recipe in d['recipes']:
        global ing_to_avoid    
        for ing in ing_to_avoid: 
            if recipe['title'].lower().find(ing) != -1 :
                d['recipes'].remove(recipe)

    d=d['recipes']
    return render_template("recipe_results.html", d = d) 

@app.route("/restaurant_search", methods=["GET"])
def rest_search():
    return render_template("restaurant_search.html")

@app.route("/restaurant_results", methods=["GET"])
def restaurant_results():
    args = request.args
    if args['cuisines']:
        cuisines = args['cuisines'].split(',')
    else:
        cuisines = []
    try:
        sort = args['sort']
    except KeyError:
        sort = 'rating'
    try:
        order = args['order']
    except KeyError:
        order = 'desc'
    if not (args['query'] or args['max_amt'] or len(cuisines) != 0):
        if args['location']:
            return redirect(url_for('rest_recc', location=args['location'])) # send location info
        else:
            return redirect(url_for('rest_recc'))
    rests = api.restaurant_search(args['query'],
            args['location'],
            args['radius'],
            args['max_amt'],
            cuisines,
            sort,
            order)
    return render_template("restaurant_results.html",
            rests = rests['restaurants'],
            num = rests['results_shown'])

@app.route("/restaurant", methods=["GET"])
def restaurant():
    try:
        rest_id = request.args['rest_id']
    except KeyError:
        flash('No restaurant id given')
        return redirect(url_for('rest_search'))
    rest = api.restaurant_info(rest_id)
    return render_template("restaurant.html",
                           rest = rest)

@app.route("/rest_recc")
def rest_recc():
    if request.args.get('location'):
        rests = api.restaurant_search('', request.args.get('location'), None, 5, [], 'rating','desc')
    else:
        rests = api.restaurant_search('', 'new york city', None, 5, [], 'rating','desc')
    return render_template("restaurant_recommendation.html",
                           rests = rests['restaurants'],
                           num = rests['results_shown'])

@app.route("/cipe_recc")
def cipe_recc():
    site= "http://food2fork.com/api/search?key=95e985762f234c8784ac3d8c57a1f3dd&"
    hdr = {'User-Agent': 'Mozilla/5.0'}

    sort_link = "sort=r"
    site += sort_link

    ing_link = "&q="
    site+=ing_link

    req = urllib2.Request(site,headers=hdr)
    uResp = urllib2.urlopen(req)

    site_content = uResp.read()

    global d 
    d = json.loads(site_content)

    d=d['recipes']
    
    return render_template("recipe_recommendation.html", d= d)

    
                           

if __name__ == "__main__":
    app.debug = True
    app.run()
