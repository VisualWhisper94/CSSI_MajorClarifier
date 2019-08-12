from app_models import Comment, value
from google.appengine.ext import ndb

ANCESTORY_KEY = ndb.Key("Comment","Comment_root")

def seed_data():
    Comment(parent=ANCESTORY_KEY,msg="This is the first comment",date=value()).put()

