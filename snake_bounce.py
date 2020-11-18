import base64
import json
import urllib
import urllib.request
from tkinter import Tk, Entry, Button, INSERT

root = Tk()
entry = Entry(root)
entry.pack()

entry.insert(INSERT, ' ')

def eocde():
    data = entry.get()
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    return str(encodedBytes, "utf-8")

def sendit():
    return "https://YOURSERVERGOESHERE/api/{}".format(eocde())

def swrap():
    with urllib.request.urlopen(sendit()) as url:
        url.read()

button = Button(root, text='send content', command=swrap)
button.pack()

root.mainloop()
