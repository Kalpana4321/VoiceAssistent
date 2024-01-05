import pyttsx3

#changing voice to a girl 
friend = pyttsx3.init()
voices = friend.getProperty('voices')
friend.setProperty('voice', voices[1].id)
friend.say("Hello guiys I am Alina, You are superb" + "A good friends always supports you and helps you when you are troubled...And A true friend always supports and loves you.")
friend.runAndWait() 