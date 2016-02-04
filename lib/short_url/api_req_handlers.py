"""MelshoX_URL_Shortener API.
By : Mahmoud Elshobaky (mahmoud.elshobaky@gmail.com)
"""
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote


# If the request contains path or querystring arguments,
# you cannot use a simple Message class.
# Instead, you must use a ResourceContainer class
REQUEST_CONTAINER = endpoints.ResourceContainer(
    message_types.VoidMessage,
    url = messages.StringField(1),
    title = messages.StringField(2),
    description = messages.StringField(3),
)


class ShortUrl(messages.Message):
    """String that stores a message."""
    url_hash = messages.StringField(1)


@endpoints.api(name='MelshoX_URL_Shortener', version='v1')
class MelshoXUrlShortApi(remote.Service):
    """MelshoX Url Short API v1."""

    @endpoints.method(REQUEST_CONTAINER, ShortUrl,
      path = "short", http_method='GET', name = "short_URL")
    def short_url(self, request):
      return ShortUrl(url_hash='abcdefg')


APPLICATION = endpoints.api_server([MelshoXUrlShortApi])
