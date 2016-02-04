from fu import *


# home page handler
class MainPage(MainHandler):
    """Home page Handler"""
    def get(self):
        self.render('index.html')
