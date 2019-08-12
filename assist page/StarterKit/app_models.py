from google.appengine.ext import ndb
import time

def value():
    t = time.localtime()
    return "{:02d}:{:02d}:{:02d}".format((t.tm_hour + 20) % 24,t.tm_min,t.tm_sec)

class Comment(ndb.Model):
    msg = ndb.StringProperty(required=True)
    date = ndb.StringProperty(default=value())