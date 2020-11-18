
##################################################################################################################
# Edit the sendit function below to replace YOURSERVERGOESHERE with your webs erver or backend server.           #
#                                                                                                                #
# Note that snake_bounce.py should basically always get an HTTP 404 when it works...                             #
#                                                                                                                #
# The idea is to use this to send the data to a server                                                           #
# in an HTTPS GET request via data packed into the URI context.                                                  #
# If the server is setup to read the request data and then                                                       #
# extract these strings, they can be encrypted server side                                                       #
# and then stored on the file system or just extracted from                                                      #
# web logs if you don't have a custom web service to do                                                          #
# that data manipulation. The logs or custom back-end                                                            #
# files on the server then can be used to access the data.                                                       #
#                                                                                                                #
# As long as your server uses HTTPS and you are not MITM'd with a proxy on a (work) network                      #
# the data you send will be encrypted in transit. There is also the potential to                                 #
# do encryption afterwards on the server side with the data, and/or before in                                    #
# another function, which is demonstrated in the snake_bounce_fernet.py version.                                 #
#                                                                                                                #
# Made for either python2 or python3                                                                             #
# anaconda python has all of these modules ready to go                                                           #
##################################################################################################################

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
