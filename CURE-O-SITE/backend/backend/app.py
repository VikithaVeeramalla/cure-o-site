import os
from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)




@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge'
    response.headers['Cache-Control'] = 'public, max-age=0, no-store'
    return response

@app.route('/')
def home():
        return render_template("final.html")
@app.route('/<id>')
def latitude(id):
    return id
