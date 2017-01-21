
from clarifai.rest import ClarifaiApp

app = ClarifaiApp("gxZl82Rccj9BDbO1py-zze9x2yXllO4K8wgtDfUv", "71dgic1AtUlwc8QX7nm6ppJojeJWqTi7pZ1K_6xy")

# get the general model
model = app.models.get("general-v1.3")

# predict with the model
response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

#response_dict = response.json()

print response["outputs"][0]["data"]["concepts"][0]["name"]

#import requests

#url = "https://www.googleapis.com/books/v1/volumes?q=Treasure%20Island"
#response = requests.get(url)
#response_dict = response.json()

#for i in range(0, 3):
#	print response_dict["items"][i]["volumeInfo"]["title"]