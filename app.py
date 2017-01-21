from flask import Flask, jsonify, render_template, request
from sort_by_date import getfiles
import requests
import time
from clarifai.rest import Image as ClImage
from clarifai.rest import ClarifaiApp
appClarifai = ClarifaiApp("gxZl82Rccj9BDbO1py-zze9x2yXllO4K8wgtDfUv", "71dgic1AtUlwc8QX7nm6ppJojeJWqTi7pZ1K_6xy")

app = Flask(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app

THRESHOLD = .7
fire_keywords = set(["flame", "fire", "smoke", "heat", "explosion", "fireplace"])
person_keywords = set(["people","adult","boy","girl", "man", "woman"])
FOLDERS = ["pictures/raymond", "pictures/treefire", "pictures/no_one", "pictures/chilling"]
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


    #response_dict = response.json()
    #print response["outputs"][0]["data"]["concepts"][0]["name"]

    folder_contents = {}
    for folder in FOLDERS:
        folder_contents[folder] = getfiles(folder)

    for image_i in range(len(folder_contents['pictures/chilling'])): # each run is one second
        responses = []

        for folder in FOLDERS: # runs the clarifai API in parallel on 4 images
            contents = folder_contents[folder]
            if image_i >= len(contents):
                image_i = -1
            image = ClImage(file_obj=open(contents[image_i], 'rb'))
            responses.append(model.predict([image]))
            time.sleep(.9)
        print len(responses)

        for response in responses:
            for i in range(0,len(response["outputs"][0]["data"]["concepts"])):
                print response["outputs"][0]["data"]["concepts"][i]["name"]
                concept = response["outputs"][0]["data"]["concepts"][i]
                name, prob = concept["name"], concept["value"]
                if name in fire_keywords and prob > THRESHOLD:
                    print "success"
                    print name
                    #return render_template("firetriggered.html") # break

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
    return render_template("map.html")






if __name__ == "__main__":
    app.run(host="0.0.0.0")
