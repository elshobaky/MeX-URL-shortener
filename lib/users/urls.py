"""
url mapping for users app a part of MelshoXblog project.
By : Mahmoud Elshobaky (mahmoud.elshobaky@gmail.com).
"""

# import app engine frameworks
import webapp2
from webapp2_extras import routes

# import app settings
from settings import *

#import project modules and request handlers
from request_handlers import *

#URL Mapping
# ex. [webapp2.Route(_u+'/signup', SignUp, 'user-signup'),]
_u = URLS_PREFIX + '/user' # you can add prefix for app ex. -u = URLS_PREFIX + '/user'
urls = [
   webapp2.Route(_u+'/signup', SignUp, 'user-signup'),
   webapp2.Route(_u+'/login', LogIn, 'user-login'),
   webapp2.Route(_u+'/logout', LogOut, 'user-logout'),
   webapp2.Route(_u+'/profile', MyProfile, 'my-profile'),
   (_u+'/([0-9]+)', Profile),
]

# rendring urls
#app = webapp2.WSGIApplication(urls,
#	config=INTERNATIONAL_CFG, debug=DEBUG)
