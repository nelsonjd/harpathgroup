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