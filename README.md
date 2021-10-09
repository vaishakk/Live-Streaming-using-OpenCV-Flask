# Secure Live Streaming of webcam footage using OpenCV and flask
Say you want to see what your dog is doing while you are out. You might think about installing a new survillance camera in your living room. Well, I say, why do you what to buy a new camera when you can repurpose one of the many cameras that you happen to have already? \
This project helps you to do just that. With this program you could use a webcam connected to your computer for survillance, streaming live feed from your home to your phone or laptop securely with support for viewing the feed simultaneously on multiple devices.

## How to?
(Only works on a Mac. To make it work on other platforms change base_url in config.py) \
On the server, make sure the webcam is connected and working. 
### Start a new virtualenv
If virtualenv not installed, install it. \
<code>
	pip install virtualenv
</code>

Start a new env. \
<code>
	python virtualenv /path/to/env
</code>

Activate env. \
<code>
	cd /path/to/env/
	source bin/activate
</code>

Install dependencies. \
<code>
	pip install -r requirements.txt 
</code>

### Config users

Add users with username and password by running the config script. \
<code>
	python config.py --user user --password password
</code>

### Run flask server

Now just run the flask app to activate the webserver. \
<code>
	python app.py
</code>

Go to 
[localhost:8848/login](http://localhost:8848/login)
to login and view webcam stream. \

To view the feed over the internet, forward tcp port 8848 on your router to the computer connected to the webcam.
