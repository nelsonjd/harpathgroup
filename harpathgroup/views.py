from flask import Flask, render_template
from . import app

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/naples")
@app.route("/naples/<name>")
def naples():
    return render_template(
        "naples.html",
    )