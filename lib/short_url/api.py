"""
API handlers for short_url app a part of MelshoXblog project.
By : Mahmoud Elshobaky (mahmoud.elshobaky@gmail.com).
"""
# import endpoints
import endpoints

# import app API Request handlers
from api_req_handlers import *

api_req_handlers = [MeXUrlShortApi]

# serve api
#APPLICATION = endpoints.api_server([MelshoXUrlShortApi])
