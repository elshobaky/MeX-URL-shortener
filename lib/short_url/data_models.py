"""
Database Models for short_url app apart of MelshoXblog project.
By : Mahmoud Elshobaky (mahmoud.elshobaky@gmail.com).
"""
import random, hashlib, datetime, logging, json
# importing google ndb datastor api
from google.appengine.ext import ndb
# user login
from google.appengine.api import users
# base ndb class
from data_model import *

# base62 hash
import base62

def urls_key(group = 'default'):
    return generate_key(name='urls', group=group)

class Url(BaseNDB):
    url = ndb.StringProperty(required=True)
    title = ndb.StringProperty()
    description = ndb.TextProperty()
    short = ndb.StringProperty()
    direct = ndb.BooleanProperty(default=False)
    user_id = ndb.IntegerProperty()

    own_key_name = 'urls'
    dict_include = None
    dict_exclude = None

    @classmethod
    def by_short(cls, short):
        uid = base62.decode(short)
        return cls.by_id(uid)

    @classmethod
    def short_url(cls,url, title, description,direct=False, user_id=None):
        u = cls(parent = urls_key(),
                url = url,
                title = title,
                description = description,
                direct=direct)
        u.put()
        u.short = base62.encode(u.key.id())
        if user_id :
            u.user_id = user_id
        u.put()
        return u
