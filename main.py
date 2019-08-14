import webapp2
import os
import jinja2
from app_model import Major, ANCESTORY_KEY
from subjects import subject_data
#from app_model import Comment, values
#from data_init import seed_data, ANCESTORY_KEY

# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
#Created a handler called MajorHandler
def GetComments():
    cmt=[]
    #for i in Comment.query(ancestor=ANCESTORY_KEY).fetch():
        #cmt.append({"comment":i.msg})
    #return cmt

class MajorHandler(webapp2.RequestHandler):
    def get(self):
        t = the_jinja_env.get_template('templates/major.html')
        values = {"comments3":GetComments()}
        self.response.write(t.render(values))
    def post(self):
        Classes = self.request.POST.items()
        failedclasses=0
        allclasses =0
        for i in Classes:
            if "class" in i[0]:
                allclasses+=1
                if float(i[1]) < 3.00:
                    failedclasses+=1

        cummlpercent = 0
        if allclasses != 0:
            cummlpercent= failedclasses / float(allclasses)






routes = [('/', MajorHandler),]
app = webapp2.WSGIApplication(routes ,debug=True)
