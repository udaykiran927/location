from flask import Flask,render_template,redirect,request
import json
import pandas as pd


app=Flask(__name__)
lat=[]
lon=[]
place=[]
@app.route("/")
def home():

    return render_template("location.html")
@app.route("/predict",methods=["POST","GET"])
def predict():
    val=[i for i in request.form.values()]
    print(val)
    lat.append(val[0])
    lon.append(val[1])
    place.append(val[2])
    Latval=val[0]
    Lonval=val[1]
    
    if((float(val[0])<=13.62960313 and float(val[1])>=13.62940313)):
        atten="Present"
    else:
        atten="Absent"
    return render_template("location.html",Latval=Latval,Lonval=Lonval,attend="Your attendence marked as: "+atten)


@app.route("/download",methods=["POST","GET"])

def download():
    d={"lattitude":lat,"longitude":lon,"place":place}
    print(d)
    df=pd.DataFrame(d)
    df.to_csv(r'C:\\Users\\udayk\\Desktop\\user2.csv')
    lat.clear()
    lon.clear()
    place.clear()
    return render_template("location.html",msg="Coordinates Downloaded")
if __name__=='__main__':
    app.run(debug=True)

