import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = {
	"q": "Hello, world!",
	"target": "es",
	"source": "en"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "34aa074b63msh02364aeff3a67b8p1dc790jsnf1aa9bccf6ae",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())