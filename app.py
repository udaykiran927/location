from flask import Flask,render_template,redirect
from urllib.request import urlopen
import json


app=Flask(__name__)
@app.route("/")
def home():
    url="http://ipinfo.io/json"
    response=urlopen(url)
    data=json.load(response)
    alloc=data["loc"]
    return render_template("index.html",alloc=alloc)

if __name__=='__main__':
    app.run(debug=True)
