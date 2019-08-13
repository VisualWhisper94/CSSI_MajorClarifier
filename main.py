import webapp2
import os
import jinja2
import ANCESTORY_KEY
# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
#Created a handler called MajorHandler
class MajorHandler(webapp2.RequestHandler):
    def get(self):
        t = the_jinja_env.get_template('templates/major.html')
        values = {"comments3":GetComments()}
        self.response.write(t.render(values))
    def GetClasses():
    Classes = []

    for i in Comment.query(ancestor=ANCESTORY_KEY).order(-Comment.date).fetch():
        Classes.append({"comment3":i.msg})

    return Classes


routes = [('/', MajorHandler),]
app = webapp2.WSGIApplication(routes ,debug=True)
