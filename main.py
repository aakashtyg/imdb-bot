import controller
import jinja2
import json
import random
import os
import urllib2
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
    ''' Main page requests handler '''

    def get(self):
        ''' GET Request for the main page '''

        # Initialize bot 
        bot = controller.Bot()

        # Get initial data
        data = bot.get_initial_data()
        self.render("index.html", data = data)

    def post(self):
        ''' POST Request for the main page '''

        input_string = json.loads(self.request.body)
        # Return dict
        jsonData = {}

        if '-' in input_string:
            # Get year
            yr = input_string.split('-', 1)[1].strip()
            # Get Movie name, and replace spaces with '+'
            movie_name = input_string.split('-', 1)[0].strip()
            movie_name = movie_name.replace(' ', '+')

            # Get the info of movie from the OMDB API (http://www.omdbapi.com/)
            movie_url = 'http://www.omdbapi.com/?t=' + movie_name + '&y=' + yr + '&r=json'
            r = urllib2.urlopen(movie_url)
            movie_info = json.loads(r.read())

            jsonData['movie'] = movie_info
            jsonData['success'] = True
            jsonData['success_msg'] = controller.SUCCESS_MSG
            self.response.out.write(json.dumps(jsonData))

        elif input_string.lower() in controller.GREETINGS_LIST:

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
