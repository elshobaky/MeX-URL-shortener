import json
# importing google ndb datastor api
from google.appengine.ext import ndb

# Generate Parent ndb Key
def generate_key(name , group = 'default'):
    return ndb.Key(name, group)

# parse DateTime Property
def date_handler(obj):
    return obj.strftime("%I:%M%p, %d. %B %Y") if hasattr(obj, 'isoformat') else obj
#Base Class for ndb DataStore
class BaseNDB(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add=True)
	last_modified = ndb.DateTimeProperty(auto_now=True)

	@classmethod
	def by_id(cls, uid, group='default'):
		return cls.get_by_id(uid, parent = generate_key(cls.own_key_name,group=group))
	
	def make_dict(cls,include=None, exclude=None):
		if cls.dict_exclude and not exclude: exclude=cls.dict_exclude
		if cls.dict_include and not include: include=cls.dict_include
		dic = cls.to_dict(include=include, exclude=exclude)
		dic['id'] = cls.key.id()
		return dic

	def make_json(cls):
		js = cls.make_dict()
		return json.dumps(js,default=date_handler)
        