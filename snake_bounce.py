'''tk GUI EaaS frontend template, tested using anaconda python(2,3)'''
import base64
import urllib.request
from tkinter import Tk, Entry, Button, INSERT

ROOT = Tk()
ROOT.title("EaaS API FrontEnd - HTTPS submit")
ENTRY = Entry(ROOT)
ENTRY.pack()
ENTRY.insert(INSERT, ' ')

# function to encode the string for URI portability
# to deal with spaces and special characters
def eocde():
    '''base64 encode the input box data for transport'''
    data = ENTRY.get()
    encbyte = base64.b64encode(data.encode("utf-8"))
    return str(encbyte, "utf-8")

# function to create the full context using the
# input string created from eocde function
def sendit():
    '''build a URI context for hard-coded URL with encoded data appended to the context'''
    return "https://YOURSERVERGOESHERE/api/{}".format(eocde())

# function to do an HTTP GET with our URL created by sendit function
def swrap():
    '''make an HTTP request with urllib for the URI context from sendit function'''
    with urllib.request.urlopen(sendit()) as url:
        url.read()

BUTTON = Button(ROOT, text='send content', command=swrap)
BUTTON.pack()

ROOT.mainloop()
