"""
url mapping for short_url app a part of MelshoXblog project.
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
_u = URLS_PREFIX + '/url' # you can add prefix for app ex. -u = URLS_PREFIX + '/page'
urls = [
   webapp2.Route(_u+'/short', ShortUrl, 'short-url'),
   ('/([a-zA-Z0-9]+)', GetUrl),
   webapp2.Route(_u+'/by-user', UserUrl, 'user-urls'),
]

# rendring urls
#app = webapp2.WSGIApplication(urls,
#	config=INTERNATIONAL_CFG, debug=DEBUG)
