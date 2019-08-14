from google.appengine.ext import ndb

class Class (ndb.Model):
    name= ndb.StringProperty(required= True)
    gpa = ndb.FloatProperty (requiered= True, defualt=0.00)

ANCESTORY_KEY= ndb.Key("Class","startkey")
gpa= 



if 
