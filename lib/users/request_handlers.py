"""
Request handlers for users app a part of MelshoXblog project.
By : Mahmoud Elshobaky (mahmoud.elshobaky@gmail.com).
"""
# importing frequently used handlers
from fu import *
# google users api
from google.appengine.api import users
# Data Models
from data_models import *


class SignUp(MainHandler):
	"""user signup handler"""
	def get(self):
		if self.user:
			role = 'u'
			if self.admin: role='admin'
			u = LocalUser.by_google_id(self.user.user_id())
			if not u:
				u = LocalUser.register(self.user.user_id(), self.user.email(), self.user.nickname(), role=role)
				u.put()
				self.write_json({'done':True,'msg':'signup successful'})
				return
			if u.role != role:
				u.role = role
				u.put()
			self.write_json({'done':False,'msg':'user already exists, user info updated'})
			return
		self.redirect_to('user-login', ref=self.uri_for('user-signup'))

class LogIn(MainHandler):
	"""user login handler"""
	def get(self):
		ref = self.request.get('ref')
		login_url = users.create_login_url(ref or '/')
		self.redirect(login_url)

class LogOut(MainHandler):
	"""user logout handler"""
	def get(self):
		logout_url = users.create_logout_url('/')
		self.redirect(logout_url)

class Profile(MainHandler):
	"""user profile handler"""
	def get(self, user_id):
		u = LocalUser.by_id(int(user_id))
		if self.user and self.user.user_id() == u.user_id:
			msg = {'my_profile' : True,
			       'user' : u.make_dict()}
			self.write_json(msg)
			return
		msg = {'user_profile' : True,
		       'user' : u.make_dict()}
		self.write_json(msg)
		return

class MyProfile(MainHandler):
	"""view and edit user own profile"""
	def get(self):
		if not self.user:
			self.redirect_to('user-login')
			return
		msg = {'my_profile' : True,
		       'user' : self.local_user.make_dict()}
		self.write_json(msg)

