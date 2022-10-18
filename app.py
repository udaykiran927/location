from flask import Flask,render_template,redirect,request
import json


app=Flask(__name__)
@app.route("/")
def home():

    return render_template("location.html")
@app.route("/predict",methods=["POST","GET"])
def predict():
    val=[i for i in request.form.values()]
    print(val)
    if((float(val[0])<=14 and float(val[0])>=13) and (float(val[1])<=79 and float(val[1])>=78)):
        atten="Present"
    else:
        atten="Absent"
    return render_template("location.html",val=val,attend="Your attendence marked as: "+atten)



if __name__=='__main__':
    app.run(debug=True)

