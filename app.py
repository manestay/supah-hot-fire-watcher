from flask import Flask, jsonify, render_template, request
import requests
import time
from clarifai.rest import Image as ClImage
from clarifai.rest import ClarifaiApp
appClarifai = ClarifaiApp("gxZl82Rccj9BDbO1py-zze9x2yXllO4K8wgtDfUv", "71dgic1AtUlwc8QX7nm6ppJojeJWqTi7pZ1K_6xy")




 


app = Flask(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app


THRESHOLD = .75
fire_keywords = set(["flame", "fire", "smoke", "heat", "explosion"])






#default home page
@app.route("/")
def hello():
    return render_template("hello.html")

#clarifai stuff
@app.route("/checkfire")
def checkfire():

    # get the general model
    model = appClarifai.models.get("general-v1.3")
    # predict with the model
    #response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
    
    image = ClImage(file_obj=open('firetest1.png', 'rb'))
    response=model.predict([image])

    #response_dict = response.json()
    #print response["outputs"][0]["data"]["concepts"][0]["name"]

    time.sleep(2) #?
    for i in range(0,len(response["outputs"][0]["data"]["concepts"])):
        print response["outputs"][0]["data"]["concepts"][i]["name"]
        concept = response["outputs"][0]["data"]["concepts"][i]
        name, prob = concept["name"], concept["value"]
        if name in fire_keywords: #and prob > THRESHOLD:
            print "success"
            print name
            #write to a textfile?
            return render_template("firetriggered.html")

    #print("entered loop")
    #for i in range(0,len(response["outputs"][0]["data"]["concepts"])):
        #print response["outputs"][0]["data"]["concepts"][i]["name"]

        #concept = response["outputs"][0]["data"]["concepts"][i]
        #name, prob = concept["name"], concept["value"]
        #if name in fire_keywords: #and prob > THRESHOLD:
            #print "success"
            #print name
            #return render_template("firetriggered.html")

    return render_template("hello.html")



#floor map updates
@app.route("/nofire")
def nofire():
    return render_template("nofire.html")


@app.route("/nopeople")
def nopeople():
    return render_template("nopeople.html")

@app.route("/oneperson")
def oneperson():
    return render_template("oneperson.html")

@app.route("/twopeople")
def twopeople():
    return render_template("twopeople.html")

@app.route("/map")
def search():
    for i in range(0,1000):
        if i%10==0:
            nofire()
        else:
            oneperson()

    return #render_template("map.html")






if __name__ == "__main__":
    app.run(host="0.0.0.0")