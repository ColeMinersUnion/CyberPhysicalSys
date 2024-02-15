#parsing through several pages on a website
import requests #alternatively people also use http.client
import cv2
import shutil
from ffpyplayer.player import MediaPlayer

#from bs4 import BeautifulSoup 
#this means that I can create a website with clues through a GitHub Pages
#This is for the Scavenger hunt
MyUri = "https://coleminersunion.github.io/assets/Images/Prize.mp4" #THe uri that I'm accessing

response = requests.get(MyUri, stream=True) #using a GET method on the URI. I didn't edit my headers. 
print(response)
with open ("Video.mp4", "wb") as file:
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file) #copies our file 

#playing the video
def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()

PlayVideo("Video.mp4")
