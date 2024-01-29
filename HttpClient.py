import requests #alternatively people also use http.client
from bs4 import BeautifulSoup 
#this means that I can create a website with clues through a GitHub Pages
#This is for the Scavenger hunt
uri = "https://coleminersunion.github.io" #THe uri that I'm accessing

session = requests.Session() #initializing a requests object.
response = session.get(uri) #using a GET method on the URI. I didn't edit my headers. 

html_soup = BeautifulSoup(response.text, 'html.parser') #i like my things readable.
print(html_soup) #seeing the html
