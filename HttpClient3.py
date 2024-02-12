#parsing through several pages on a website
import requests #alternatively people also use http.client
import cv2
import shutil

#from bs4 import BeautifulSoup 
#this means that I can create a website with clues through a GitHub Pages
#This is for the Scavenger hunt
MyUri = "https://coleminersunion.github.io/assets/Images/Prize.mp4" #THe uri that I'm accessing

response = requests.get(MyUri, stream=True) #using a GET method on the URI. I didn't edit my headers. 
print(response)
with open ("Video.mp4", "wb") as file:
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)

#playing the video
capture = cv2.VideoCapture("Video.mp4")
if (capture.isOpened()== False): 
    print("Error opening video file") 
  
# Read until video is completed 
while(capture.isOpened()): 
      
# Capture frame-by-frame 
    ret, frame = capture.read() 
    if ret == True: 
    # Display the resulting frame 
        cv2.imshow('Frame', frame) 
          
    # Press Q on keyboard to exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
  
# Break the loop 
    else: 
        break
  
# When everything done, release 
# the video capture object 
capture.release() 
  
# Closes all the frames 
cv2.destroyAllWindows() 
#now we can send different urls and edit the url several times to get an assortment of data
