from flask import Flask, jsonify, render_template, request
import requests


from clarifai.rest import ClarifaiApp

appClarifai = ClarifaiApp("gxZl82Rccj9BDbO1py-zze9x2yXllO4K8wgtDfUv", "71dgic1AtUlwc8QX7nm6ppJojeJWqTi7pZ1K_6xy")





app = Flask(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app

@app.route("/")
def hello():
    # get the general model
    model = appClarifai.models.get("general-v1.3")
    # predict with the model
    response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
    #response_dict = response.json()
    #print response["outputs"][0]["data"]["concepts"][0]["name"]
    for i in range(0,len(response["outputs"][0]["data"]["concepts"])):
        name = response["outputs"][0]["data"]["concepts"][i]["name"]
        if name == "flame" or name == "fire" or name 

    return render_template("hello.html", api_data=response)

@app.route("/name")
def name():
	return "Your Name"

@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        url = "https://www.googleapis.com/books/v1/volumes?q=" + request.form["user_search"]
        response_dict = requests.get(url).json()
        return render_template("results.html", api_data=response_dict)
    else: # request.method == "GET"
        return render_template("search.html")



@app.route("/searchtime", methods=["POST", "GET"])
def searchtime():
    if request.method == "POST":
        url = "https://www.googleapis.com/books/v1/volumes?q=" + request.form["user_search"]
        response_dict = requests.get(url).json()
        return render_template("timeresults.html", api_data=response_dict, hours=float(request.form["user_searchtime"] ) )
    else: # request.method == "GET"
        return render_template("searchtime.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")