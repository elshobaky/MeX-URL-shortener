"""
url mapping for MelshoXblog project.
By : Mahmoud Elshobaky (mahmoud.elshobaky@gmail.com).
"""

# import app engine frameworks
import webapp2
from webapp2_extras import routes
# import app settings
from settings import *

#import project modules /apps and request handlers
from fu import *
from home import *
# Mapping
_u = URLS_PREFIX
urls = [
    webapp2.Route(_u+'/', MainPage, 'home-page'),
    webapp2.Route(_u+'/switch-lang', Locale, 'language-switsh'),
]

# importing project apps urls
from lib import users, short_url
# importing urls from each app
from users import urls as users_urls
from short_url import urls as short_url_urls

urls += users_urls.urls
urls += short_url_urls.urls

# rendring urls
app = webapp2.WSGIApplication(urls,
	config=INTERNATIONAL_CFG, debug=DEBUG)
