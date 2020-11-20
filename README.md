![snake_bounce](https://carefuldata.com/images/cdlogo.png)

# snake_bounce
python front-end TK minimal interface for sending data in HTTP GET requests via string appended to URI context

Edit the sendit function to replace YOURSERVERGOESHERE with your webserver or backend server. 
If you are on a unix based system like mac, linux, or bsd, you can use the included sh_sb program
to configure a copy that is edited automatically:

chmod +x sh_sb

./sh_sb $YOURURL

Note that if you just send to a default NGINX or Apache2 server configuration,
the data will be stored to disk and readable by the administrator 
or anyone who has access to that disk of the server
because base64 is not encryption, just there for transport in this case.

## See https://github.com/jpegleg/badger-chainz for example server data configuration
Store the web logs to disk and then pipe data from memory into a
local block chain or just file organizing, with optional configurable encryption layers.

###### Note that snake bounce should basically always get an HTTP 404 when it works...           

 The idea is to use this to send the data to a server                                                      
 in an HTTPS GET request via data packed into the URI context.                                              
 If the server is setup to read the request data and then                                                 
 extract these strings, they can be encrypted server side                                                    
 and then stored on the file system or just extracted from                                                   
 web logs if you don't have a custom web service to do                                                      
 that data manipulation. The logs or custom back-end                                                          
 files on the server then can be used to access the data.                                                    
                                                                                                              
 As long as your server uses HTTPS and you are not MITM'd with a proxy on a (work) network                    
 the data you send will be encrypted in transit. There is also the potential to                               
 do encryption afterwards on the server side with the data, and/or before in                                
 another function etc.                           
                                                                                                           
###### Made for either python2 or python3   
                                                                    
 Anaconda python has all of the modules ready to go.



