import pytest
from User import *

def test_auth_user():
	user = User()
	user.id = 'vk'
	assert user.auth_user('alphabc') == True