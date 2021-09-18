from flask import Flask, render_template, Response, request
import flask
import cv2
import threading
import atexit
from User import User
import flask_login

app = Flask(__name__)
app.secret_key = 'tangocasa'
camera = cv2.VideoCapture(0)  # use 0 for web camera
frame = None

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def user_loader(user):
    user = User()
    user.id = user
    return user


@login_manager.request_loader
def request_loader(request):
    user = request.form.get('user')
    user = User()
    user.id = user
    user.is_authenticated = user.auth_user(request.form['password'])

    return user

def gen_frames():  # generate frame by frame from camera
# Capture frame-by-frame    
    global frame
    success, f = camera.read()  # read the camera frame
    if success:
        ret, buffer = cv2.imencode('.jpg', f)
        frame = buffer.tobytes()
    threading.Timer(0.03, gen_frames).start()

def feed_frame():
    while True:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(feed_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/stream')
@flask_login.login_required
def stream():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='user' id='user' placeholder='User Name'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    print(request.form)
    user = User()
    user.id = request.form['user']
    if user.auth_user(request.form['password']):
        flask_login.login_user(user)
        #print(flask.url_for('stream'))
        return flask.redirect(flask.url_for('stream'))
    return 'Bad login'


@atexit.register
def exitfunc():
    global camera
    camera.release()
    print('Closing...')

if __name__ == '__main__':
    gen_frames()
    app.run(host='0.0.0.0', port=8848)