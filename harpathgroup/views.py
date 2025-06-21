from flask import Flask, render_template
from . import app
from .db_runner import query_db

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/locations")
def locations():
    return render_template(
        "locations.html",
    )

@app.route("/locations/")
@app.route("/locations/<identifier>")
def locations_show(identifier=None):
    location = query_db('select * from locations where identifier = ?', [identifier], one=True)

    if location is None: 
        return 'No such location'
        
    
    return render_template(
        "locations_show.html",
        location=location
    )
