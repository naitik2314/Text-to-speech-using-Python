# Import the library you just installed
from gtts import gTTS 

# import os to access the directory.
import os 

# The text that you want to convert to audio 
mytext = 'Welcome to my channel, I am Naitik Shah, and this is not my real voice though'

# Language in which you want to convert 
language = 'en'

#This is the magic line
myobj = gTTS(text=mytext, lang=language, slow=False) 

##To save the file, you may give any file you want
myobj.save("welcome.mp3") 

# Playing the converted file 
#os.system("mpg321 welcome.mp3") 

