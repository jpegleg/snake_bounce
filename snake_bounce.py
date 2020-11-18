import base64
import json
import urllib
import urllib.request
from tkinter import Tk, Entry, Button, INSERT

root = Tk()
entry = Entry(root)
entry.pack()

entry.insert(INSERT, ' ')

# function to encode the string for URI portability
# to deal with spaces and special characters
def eocde():
    data = entry.get()
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    return str(encodedBytes, "utf-8")

# function to create the full context using the 
# input string created from eocde function
def sendit():
    return "https://YOURSERVERGOESHERE/api/{}".format(eocde())

# function to do an HTTP GET with our URL created by sendit function
def swrap():
    with urllib.request.urlopen(sendit()) as url:
        url.read()

button = Button(root, text='send content', command=swrap)
button.pack()

root.mainloop()
