import flask_login
import hashlib
import os
import json

base_path = '/Library/Application Support/Live WebCam/'
if not os.path.isfile(os.path.join(base_path, 'config.config')):
    users  = {}
else:
    with open(os.path.join(base_path, 'config.config'),'r') as file:
        users = json.load(file)

class User(flask_login.UserMixin):
    def auth_user(self, password):
        global users
        if self.id in users:
            salt = users[self.id]['salt'].encode('utf-8')
            key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
            if key.decode('latin-1') == users[self.id]['key']:
                return True
        return False
