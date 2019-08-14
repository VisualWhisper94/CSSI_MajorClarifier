import webapp2
import os
import jinja2

#from data_init import seed_data, ANCESTORY_KEY

# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#Values dictionary is holds templates variables
values = {"majors":["History","Mathematics","English","Liberal Arts","Computer Science","Other"]}
#Created a handler called MajorHandler

def CompileClassData(elements):
    values["failed"] = 0
    values["passed"] = 0
    values["count"] = 0
    values["classes"] = []
    
    i = 0
    n = len(elements)

    if elements[0][1] == "Other":
        values["major"] = elements[1][1]
    else:
        values["major"] = elements[0][1]
    
    while i < n:
        if "class" in elements[i][0]:
            values["count"] += 1

            if float(elements[i+1][1]) < 3.00:
                values["failed"] += 1
                values["classes"].append((elements[i][1],elements[i+1][1],"failed"))
            else:
                values["passed"] += 1
                values["classes"].append((elements[i][1],elements[i+1][1],"passed"))

        i += 1 

    if values["count"] <= 15:
        values["status"] = "Lower Freshman"
    elif values["count"] <= 30:
        values["status"] = "Upper Freshman"
    elif values["count"] <= 45:
        values["status"] = "Lower Sophomore"
    elif values["count"] <= 60:
        values["status"] = "Upper Sophomore"
    elif values["count"] <= 75:
        values["status"] = "Lower Junior"
    elif values["count"] <= 90:
        values["status"] = "Upper Junior"
    elif values["count"] <= 105:
        values["status"] = "Lower Senior"
    elif values["count"] <= 120:
        values["status"] = "Upper Senior"
    else:
        values["status"] = "Post Graduate"
    
def Suggestion(percent):
    if values["count"] == 0:
        values["suggestions"] = "Please register for classes."
    elif percent <= 0.25:
        values["suggestions"] = "You are on track. Keep up the pace."
    elif percent >= 0.275 and percent < 0.5:
        values["suggestions"] = "You may need help keeping up the pace. Consider finding external help such as tutoring."
    else:
        values["suggestions"] = "You may need to consider switching your major. Please speak to your advisor for further help."

class MajorHandler(webapp2.RequestHandler):
    def get(self):
        t = the_jinja_env.get_template('templates/index2.html')
        self.response.write(t.render(values))

    def post(self):
        t = the_jinja_env.get_template('/templates/results2.html')
        classes = self.request.POST.items()
        CompileClassData(classes)
        
        cummlpercent = 0

        if values["count"] != 0:
            cummlpercent = values["failed"] / float(values["count"])
        
        Suggestion(cummlpercent)

        self.response.write(t.render(values))

class EmailHandler(webapp2.RequestHandler):
    def get(self):
        t = the_jinja_env.get_template('templates/email.html')
        self.response.write(t.render())


routes = [
    ('/', MajorHandler),
    ('/email', EmailHandler)
    ]
app = webapp2.WSGIApplication( routes , debug=True)
