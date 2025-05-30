from flask import Flask, render_template
from . import app

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/locations")
def locations():
    return render_template(
        "locations.html",
    )

@app.route("/locations/")
@app.route("/locations/<location>")
def locations_show(location=None):
    return render_template(
        "locations_show.html",
        location=location
    )
