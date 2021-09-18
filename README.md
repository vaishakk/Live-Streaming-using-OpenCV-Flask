# Secure Live Streaming of webcam footage using OpenCV and flask
A Flask Web-App to stream live from local webcam. Users can added with username and passowrd to enable secure login. Only logged in users can view the stream.

## How to?
On the server, make sure the webcam is connected and working. 
### Start a new virtualenv
If virtualenv not installed, install it.

<code>
	pip install virtualenv
</code>

Start a new env

<code>
	python virtualenv /path/to/env
</code>

Install dependencies.

<code>
	pip install -r requirements.txt 
</code>

### Config users

Add users with username and password by running the config script.

<code>
	python config.py --user user --password password
</code>

### Run flask server

Now just run the flask app to activate the webserver.

<code>
	python app.py
</code>
