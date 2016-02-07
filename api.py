"""
API Handlers  for MelshoXblog project.
By : Mahmoud Elshobaky (mahmoud.elshobaky@gmail.com).
"""
# import endpoints
import endpoints
api_handlers = []
# import project API Request handlers from each project app

from lib import short_url #, users
from short_url import api as short_url_api

api_handlers += short_url_api.api_handlers

# serve API
APPLICATION = endpoints.api_server(api_handlers)
