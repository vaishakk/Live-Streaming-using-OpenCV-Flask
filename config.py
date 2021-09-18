import os
import argparse
import hashlib
import json
import random

alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
base_path = '/Library/Application Support/Live WebCam/'
if not os.path.isfile(os.path.join(base_path, 'config.config')):
	users  = {}
	if not os.path.isdir(base_path):
		os.mkdir(base_path)
else:
	with open(os.path.join(base_path, 'config.config'),'r') as file:
		users = json.load(file)

my_parser = argparse.ArgumentParser(description='Config Live WebCam')

# Add the arguments
my_parser.add_argument('--user',
                       metavar='user',
                       type=str,
                       help='username',
                       required=True)
my_parser.add_argument('--password',
                       metavar='password',
                       type=str,
                       help='password',
                       required=True)

args = my_parser.parse_args()
user = args.user 
password = args.password


#salt = os.urandom(32)
salt = ''.join((random.choice(alphabets)) for i in range(32))
#salt = salt.decode('utf-8') # A new salt for this user
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)

print(key)
users[user] = { # Store the salt and key
    'salt': salt,
    'key': key.decode('latin-1')
}
with open(os.path.join(base_path, 'config.config'),'w') as file:
	json.dump(users, file)