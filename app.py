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
fire_keywords = set(["flame", "fire", "smoke", "heat", "explosion"])
person_keywords = set(["people", "adult","boy","girl", "man", "woman"])
FOLDERS = ["pictures/raymond", "pictures/treefire", "pictures/chilling"]
#default home page
@app.route("/")
def hello():
    return render_template("hello.html")

#clarifai stuff
@app.route("/checkfire")
def checkfire():
    fires, people = 0, 0

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
            if fires == 2 and folder == "pictures/treefire": continue # skip to save API call time, since fire never goes out in tree fire
            responses.append(model.predict([image]))
            print contents[image_i]
        time.sleep(.9)

        people = 0
        for response in responses:
            for i in range(0,len(response["outputs"][0]["data"]["concepts"])):
                concept = response["outputs"][0]["data"]["concepts"][i]
                name, prob = concept["name"], concept["value"]
                if name in fire_keywords and fires < 2:
                    fires += 1
                    break
                if name in person_keywords:
                    people += 1
                    break
        print fires, people
        update_file(fires, people)

    return render_template("hello.html")

def update_file(fires, people):
    text_file = open("static/testthis.txt", "w")
    if fires == 0: # case 1
        output = 1
    elif fires == 1 and people >= 2: # case 2
        output = 2
    elif fires == 2 and people >= 2:
        output = 3
    elif fires == 2 and people == 1:
        output = 4
    else:
        output = -1
        print "error!!!"
    text_file.write("%s" % output)
    text_file.close()

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

if __name__ == "__main__":
    app.run(host="0.0.0.0")
