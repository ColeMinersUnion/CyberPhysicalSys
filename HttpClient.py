#parsing through several pages on a website
import requests #alternatively people also use http.client
from bs4 import BeautifulSoup 
#this means that I can create a website with clues through a GitHub Pages
#This is for the Scavenger hunt
MyUri = "https://ProfessionalGooseChaser.github.io" #THe uri that I'm accessing

def getPageInfo(uri):
    session = requests.Session() #initializing a requests object.
    response = session.get(uri) #using a GET method on the URI. I didn't edit my headers. 

    html_soup = BeautifulSoup(response.text, 'html.parser') #i like my things readable.
    return html_soup #seeing the html
print(getPageInfo(MyUri))
#now we can send different urls and edit the url several times to get an assortment of data