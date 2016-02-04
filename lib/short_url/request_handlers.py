"""
Request handlers for short_url app a part of MelshoXblog project.
By : Mahmoud Elshobaky (mahmoud.elshobaky@gmail.com).
"""
# importing frequently used handlers
from fu import *
_ = t
# Data Models
from data_models import *

class ShortUrl(MainHandler):
    def get(self):
        url = self.request.get('url')
        title = self.request.get('title')
        description = self.request.get('description')
        direct = self.request.get('direct')
        if direct == "true":
            direct = True
        else:
            direct = False
        if not valid_url(url):
            res = {'error': {'error':'URL not valid'},
                   'url': url,
                   'title': title,
                   'description': description}
            self.write_json(res)
            return
        if self.local_user :
            user_id = self.local_user.key.id()
        else:
            user_id = None
        u = Url.short_url(url, title, description,direct=direct, user_id=user_id)
        self.write_json(u.make_json())
        return

class GetUrl(MainHandler):
    def get(self, short):
        u = Url.by_short(short)
        if u:
            if u.direct:
                self.redirect(str(u.url))
                return
            self.render('redirect.html', url=u)
            return
        res = {'error':{'error':'Not Found'}}
        self.write_json(res)
        return
