from flask import Flask,render_template,redirect
from urllib.request import urlopen
import json


app=Flask(__name__)
@app.route("/")
def home():
    
    return render_template("location.html")

if __name__=='__main__':
    app.run(debug=True)
