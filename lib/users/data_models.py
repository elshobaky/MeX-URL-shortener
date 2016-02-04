"""
Database Models for users app apart of MelshoXblog project.
By : Mahmoud Elshobaky (mahmoud.elshobaky@gmail.com).
"""
import random, hashlib, datetime, logging, json
# importing google ndb datastor api
from google.appengine.ext import ndb
# user login
from google.appengine.api import users
# project settings
from settings import *
# base ndb class
from data_model import *


def users_key(group = 'default'):
    return generate_key(name='users', group=group)

class LocalUser(BaseNDB):
	user_id = ndb.StringProperty()
	role = ndb.StringProperty(default='u')
	email = ndb.StringProperty()
	nickname = ndb.StringProperty()
	locale = ndb.StringProperty(default=LOCALE)

	own_key_name = 'users'
	dict_include = None
	dict_exclude = ['user_id', 'role','created', 'last_modified']

	@classmethod
	def by_google_id(cls, uid):
		return cls.query().filter(cls.user_id == uid).get()

	@classmethod
	def register(cls, user_id, email, nickname, role = 'u', group = 'default'):
		return cls(parent = users_key(group=group),
			       user_id = user_id,
			       email = email,
			       nickname = nickname,
			       role = role)

	@classmethod
	def update_info(cls, locale='ar-EG'):
		return cls(locale=locale)