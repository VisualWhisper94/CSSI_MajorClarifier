import webapp2
import jinja2
import os
from app_models import Comment, value
from data_init import seed_data, ANCESTORY_KEY

jinja_env =  jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True) 

def GetComments():
    cmt = []
    
    for i in Comment.query(ancestor=ANCESTORY_KEY).order(-Comment.date).fetch():
        cmt.append({"comment":i.msg,"time":i.date})
    
    return cmt

class MainPage(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template('/templates/index.html')
        seed_data()
        vals = {"comments":GetComments()}
        self.response.write(t.render(vals))

    def post(self):
        t = jinja_env.get_template('/templates/index.html')
        msg = self.request.get("comment")
        if msg != "" :
            Comment(parent=ANCESTORY_KEY,msg=msg,date=value()).put()
        vals = {"comments":GetComments()}
        self.response.write(t.render(vals))

routes = [('/',MainPage)]
app = webapp2.WSGIApplication(routes, debug=True)

