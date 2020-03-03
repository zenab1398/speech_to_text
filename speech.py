from gtts import gTTS 
import os 

import speech_recognition as sr 
x=int(input("enter a value"))
if x==1:
    print("speech to text")
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("SAY SOMETHING")
        audio=r.listen(source)
        #print("TIME OVER, THANKS")
    try:
        print("TEXT : "+r.recognize_google(audio))
    except:
        pass
else:
    print("text to speech")
    # The text that you want to convert to audio 
    mytext =input('enter text')
    
    # Language in which you want to convert 
    language = 'en'
    
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("welcome.mp3") 
    
    # Playing the converted file 
    os.system("welcome.mp3") 