from flask import Flask, session, url_for, redirect, render_template, request
import urllib2
import requests
import json
#import api

#App instantiation
app = Flask(__name__)

d = {}
ingredients = []
ing_to_avoid = []

@app.route("/")
def homepage():
    return render_template("home.html")


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

    global d 
    if (d['count'] == 0):
        #print("no results")
        site = "http://food2fork.com/api/search?key=95e985762f234c8784ac3d8c57a1f3dd&"
        if (sort_link == "sort=r"):
            message = "Oops, looks like there were no hightest rating recipes with the entered ingredients. Check to see if there are trendy recipes instead?"
            sort_link = "sort=t"
        else:
            message = "Oops, looks like there were no trendy recipes with the entered ingredients. Check to see if there are highest rating recipes instead?"
            sort_link = "sort=r"
            
        site += sort_link 
        site += ing_link
        #print ("new site:" + site) 
        req = urllib2.Request(site,headers=hdr)
        uResp = urllib2.urlopen(req)

        #Grabbing information
        site_content = uResp.read()

        #Turning grabebd information into a dictionary
        global d 
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

    global d
    d=d['recipes']
    return render_template("recipe_results.html", d = d) 

        
        
if __name__ == "__main__":
    app.debug = True
    app.run()
