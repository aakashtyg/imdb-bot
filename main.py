import controller
import jinja2
import json
import random
import os 
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kwargs):
        self.response.out.write(*a, **kwargs)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))

class MainPage(Handler):

    def get(self):
        print "IN GET"
        # Initialize bot 
        bot = controller.Bot()

        # Get initial data
        data = bot.get_initial_data()
        self.render("index.html", data = data)

    def post(self):
        print "IN post"
        input_string = json.loads(self.request.body)
        # Return dict
        jsonData = {}

        if '-' in input_string:
            # Get year
            yr = input_string.split('-', 1)[1].strip()
            # Get Movie name
            movie_name = input_string.split(' ', 2)[1].strip()

            # Get data from OMDB API

            jsonData['success'] = True
            jsonData['success_msg'] = controller.SUCCESS_MSG
            self.response.out.write(json.dumps(jsonData))
        elif input_string.lower() in controller.GREETINGS_LIST:
            print "hwerw"
            jsonData['success'] = True
            jsonData['success_msg'] = random.choice(controller.GREETINGS_RESPONSE_LIST)
            return self.response.out.write(json.dumps(jsonData))
        else:
            jsonData['error'] = True
            jsonData['error_msg'] = controller.ERROR_MSG
            self.response.out.write(json.dumps(jsonData))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
