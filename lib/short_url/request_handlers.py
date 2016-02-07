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
    def post(self):
        self.url = self.request.get('url')
        self.multi_url = self.request.get('multi_url')
        self.title = self.request.get('title')
        self.description = self.request.get('description')
        self.direct = self.request.get('direct')
        if self.direct == "true":
            self.direct = True
        else:
            self.direct = False
        if self.local_user :
            self.user_id = self.local_user.key.id()
        else:
            self.user_id = None
        if self.multi_url != "false":
            self.short_multi()
            return
        if not valid_url(self.url):
            res = {'error': {'error':'URL not valid'},
                   'url': self.url,
                   'title': self.title,
                   'description': self.description}
            self.write_json(res)
            return
        u = Url.short_url(self.url, self.title, self.description,direct=self.direct, user_id=self.user_id)
        self.write_json(u.make_json())
        return
    def short_multi(self):
        to_short = self.multi_url.split('\n')
        shortened = []
        for u in to_short:
            if not valid_url(u):
                shortened.append(['error','not valid url ("{}")'.format(u)])
                continue
            u_shortened = Url.short_url(u, self.title, self.description,direct=self.direct, user_id=self.user_id)
            shortened.append(['success',u_shortened.short])
        self.write_json({'multi_short':True, 'urls':shortened})

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
