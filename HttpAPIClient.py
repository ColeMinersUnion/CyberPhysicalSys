import requests

url = "https://national-weather-service.p.rapidapi.com/stations/KIH35"

headers = {
	"X-RapidAPI-Key": "34aa074b63msh02364aeff3a67b8p1dc790jsnf1aa9bccf6ae",
	"X-RapidAPI-Host": "national-weather-service.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())