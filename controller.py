SUCCESS = 'Success'
FAIL = 'Fail'
WELCOME_MSG = '''Hello there, you can get info on any movie you like \
               Movie <movie_name> - <year>'''
ERROR_MSG = '''Sorry we couldn't find that movie'''
SUCCESS_MSG = '''Please wait, we are getting your data '''
GREETINGS_LIST = ['hello', 'sup', 'hola', 'sup bro', 'yo']
GREETINGS_RESPONSE_LIST = ['Hello', 'Yo', 'I am fine']

class Bot:

    def __init__(self):
        self.name = 'imdb_bot'

    def get_initial_data(self):
        data = {}
        data['welcome_msg'] = WELCOME_MSG

        return data

