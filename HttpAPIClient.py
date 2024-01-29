import requests

url = "https://api-basketball.p.rapidapi.com/games"

querystring = {"date":"2019-11-26"}

headers = {
	"X-RapidAPI-Key": "34aa074b63msh02364aeff3a67b8p1dc790jsnf1aa9bccf6ae",
	"X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())