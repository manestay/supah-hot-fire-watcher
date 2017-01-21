import requests

url = "https://www.googleapis.com/books/v1/volumes?q=Treasure%20Island"
response = requests.get(url)
response_dict = response.json()

for i in range(0, 3):
	print response_dict["items"][i]["volumeInfo"]["title"]