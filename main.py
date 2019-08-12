import webapp2
import os
import jinja2

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MajorHandler(webapp2.RequestHandler):
    """docstring for ."""
    def get(self):
        t = the_jinja_env.get_template('templates/major.html')
        self.response.write(t.render())

routes = [('/', MajorHandler),]
app = webapp2.WSGIApplication(routes ,debug=True)
