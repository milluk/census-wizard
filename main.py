import cgi
import os

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template

class Entry(db.Model):
  author          = db.UserProperty()
  date            = db.DateTimeProperty(auto_now=True)
  address         = db.StringProperty(multiline=True)
  num_residents   = db.StringProperty()
  last_name       = db.StringProperty()
  first_name      = db.StringProperty()
  middle_initial  = db.StringProperty()

class MainPage(webapp.RequestHandler):
  def get(self):
    # FIXME: pull back only the row(s) related to the current user
    entries_query = Entry.all()
    entry = entries_query.get()

    if users.get_current_user():
      url = users.create_logout_url(self.request.uri)
      url_linktext = 'Logout'
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'Login'

    template_values = {
      'entry': entry,
      'url': url,
      'url_linktext': url_linktext,
      }

    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))
    
class Guestbook(webapp.RequestHandler):
  def post(self):
    # we were given a key, try to get the entry associated with it
    key = self.request.get('entry_key', '')
    entry = Entry()
    if key != '':
        entry = Entry.get(self.request.get('entry_key'))
    if entry is None:
        entry = Entry()


    entry.author = users.get_current_user()

    entry.address        = self.request.get('address')
    entry.num_residents  = self.request.get('num_residents')

    entry.last_name      = self.request.get('last_name')
    entry.first_name     = self.request.get('first_name')
    entry.middle_initial = self.request.get('middle_initial')

    entry.put()
    self.redirect('/')

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/sign', Guestbook)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
