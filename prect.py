# print('''
#       Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the trav'ller in the dark,
# Thanks you for your tiny spark,
# He could not see which way to go,
# If you did not twinkle so.

# In the dark blue sky you keep,
# And often thro' my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.

# 'Tis your bright and tiny spark,
# Lights the trav'ller in the dark:
# Tho' I know not what you are,
# Twinkle, twinkle, little star.''')
# import Tensors 

# x = Tensors.rand(5, 3)
# print(x)
# import requests
# response = requests.get("https://www.geeksforgeeks.org/python/python-requests-tutorial/")
# print(response.status_code)
# print(response.text)
# import pyttsx3
# engine = pyttsx3.init()

# # For Mac, If you face error related to "pyobjc" when running the `init()` method :
# # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# engine.say("I will speak this text it is a text to speech conversion example using pyttsx3 library in python.because it is an offline library it does not require internet connection to work.")
# engine.runAndWait()
import os

def list_directory_contents(path='.'):
    try:
        contents = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for item in contents:
            print(item)
    except Exception as e:
        print(f"Error: {e}")

# Example usage
list_directory_contents('/path/to/your/directory')