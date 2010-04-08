import os
import json
import cgi
import sys

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template

shared_secrety_api_key = '<SHARED SECRET HERE>'

class Entry(db.Model):
  author            = db.UserProperty()
  date              = db.DateTimeProperty(auto_now=True)

  unique_key        = db.StringProperty()
  first_name        = db.StringProperty()
  last_name         = db.StringProperty()
  email             = db.StringProperty()
  phone             = db.StringProperty()
  address           = db.StringProperty(multiline=True)
  streetaddress     = db.StringProperty()
  streetaddress2    = db.StringProperty()
  city              = db.StringProperty()
  state             = db.StringProperty()
  zip               = db.StringProperty()
  ownership         = db.StringProperty()
  num_residents     = db.StringProperty()

  # wow, it would be really nice if I knew how to dynamically define a class in python

  p00_last_name         = db.StringProperty()
  p00_first_name        = db.StringProperty()
  p00_middle_initial    = db.StringProperty()
  p00_sex               = db.StringProperty()
  p00_birth_date        = db.StringProperty()
  p00_birth_month       = db.StringProperty()
  p00_birth_day         = db.StringProperty()
  p00_birth_year        = db.StringProperty()
  p00_hispanic          = db.StringProperty()
  p00_race              = db.StringProperty()
  p00_usual_residence   = db.StringProperty()
  p00_relation          = db.StringProperty()

  p01_last_name         = db.StringProperty()
  p01_first_name        = db.StringProperty()
  p01_middle_initial    = db.StringProperty()
  p01_sex               = db.StringProperty()
  p01_birth_date        = db.StringProperty()
  p01_birth_month       = db.StringProperty()
  p01_birth_day         = db.StringProperty()
  p01_birth_year        = db.StringProperty()
  p01_hispanic          = db.StringProperty()
  p01_race              = db.StringProperty()
  p01_usual_residence   = db.StringProperty()
  p01_relation          = db.StringProperty()

  p02_last_name         = db.StringProperty()
  p02_first_name        = db.StringProperty()
  p02_middle_initial    = db.StringProperty()
  p02_sex               = db.StringProperty()
  p02_birth_date        = db.StringProperty()
  p02_birth_month       = db.StringProperty()
  p02_birth_day         = db.StringProperty()
  p02_birth_year        = db.StringProperty()
  p02_hispanic          = db.StringProperty()
  p02_race              = db.StringProperty()
  p02_usual_residence   = db.StringProperty()
  p02_relation          = db.StringProperty()

  p03_last_name         = db.StringProperty()
  p03_first_name        = db.StringProperty()
  p03_middle_initial    = db.StringProperty()
  p03_sex               = db.StringProperty()
  p03_birth_date        = db.StringProperty()
  p03_birth_month       = db.StringProperty()
  p03_birth_day         = db.StringProperty()
  p03_birth_year        = db.StringProperty()
  p03_hispanic          = db.StringProperty()
  p03_race              = db.StringProperty()
  p03_usual_residence   = db.StringProperty()
  p03_relation          = db.StringProperty()

  p04_last_name         = db.StringProperty()
  p04_first_name        = db.StringProperty()
  p04_middle_initial    = db.StringProperty()
  p04_sex               = db.StringProperty()
  p04_birth_date        = db.StringProperty()
  p04_birth_month       = db.StringProperty()
  p04_birth_day         = db.StringProperty()
  p04_birth_year        = db.StringProperty()
  p04_hispanic          = db.StringProperty()
  p04_race              = db.StringProperty()
  p04_usual_residence   = db.StringProperty()
  p04_relation          = db.StringProperty()

  p05_last_name         = db.StringProperty()
  p05_first_name        = db.StringProperty()
  p05_middle_initial    = db.StringProperty()
  p05_sex               = db.StringProperty()
  p05_birth_date        = db.StringProperty()
  p05_birth_month       = db.StringProperty()
  p05_birth_day         = db.StringProperty()
  p05_birth_year        = db.StringProperty()
  p05_hispanic          = db.StringProperty()
  p05_race              = db.StringProperty()
  p05_usual_residence   = db.StringProperty()
  p05_relation          = db.StringProperty()

  p06_last_name         = db.StringProperty()
  p06_first_name        = db.StringProperty()
  p06_middle_initial    = db.StringProperty()
  p06_sex               = db.StringProperty()
  p06_birth_date        = db.StringProperty()
  p06_birth_month       = db.StringProperty()
  p06_birth_day         = db.StringProperty()
  p06_birth_year        = db.StringProperty()
  p06_hispanic          = db.StringProperty()
  p06_race              = db.StringProperty()
  p06_usual_residence   = db.StringProperty()
  p06_relation          = db.StringProperty()

  p07_last_name         = db.StringProperty()
  p07_first_name        = db.StringProperty()
  p07_middle_initial    = db.StringProperty()
  p07_sex               = db.StringProperty()
  p07_birth_date        = db.StringProperty()
  p07_birth_month       = db.StringProperty()
  p07_birth_day         = db.StringProperty()
  p07_birth_year        = db.StringProperty()
  p07_hispanic          = db.StringProperty()
  p07_race              = db.StringProperty()
  p07_usual_residence   = db.StringProperty()
  p07_relation          = db.StringProperty()

  p08_last_name         = db.StringProperty()
  p08_first_name        = db.StringProperty()
  p08_middle_initial    = db.StringProperty()
  p08_sex               = db.StringProperty()
  p08_birth_date        = db.StringProperty()
  p08_birth_month       = db.StringProperty()
  p08_birth_day         = db.StringProperty()
  p08_birth_year        = db.StringProperty()
  p08_hispanic          = db.StringProperty()
  p08_race              = db.StringProperty()
  p08_usual_residence   = db.StringProperty()
  p08_relation          = db.StringProperty()

  p09_last_name         = db.StringProperty()
  p09_first_name        = db.StringProperty()
  p09_middle_initial    = db.StringProperty()
  p09_sex               = db.StringProperty()
  p09_birth_date        = db.StringProperty()
  p09_birth_month       = db.StringProperty()
  p09_birth_day         = db.StringProperty()
  p09_birth_year        = db.StringProperty()
  p09_hispanic          = db.StringProperty()
  p09_race              = db.StringProperty()
  p09_usual_residence   = db.StringProperty()
  p09_relation          = db.StringProperty()

  p10_last_name         = db.StringProperty()
  p10_first_name        = db.StringProperty()
  p10_middle_initial    = db.StringProperty()
  p10_sex               = db.StringProperty()
  p10_birth_date        = db.StringProperty()
  p10_birth_month       = db.StringProperty()
  p10_birth_day         = db.StringProperty()
  p10_birth_year        = db.StringProperty()
  p10_hispanic          = db.StringProperty()
  p10_race              = db.StringProperty()
  p10_usual_residence   = db.StringProperty()
  p10_relation          = db.StringProperty()

  p11_last_name         = db.StringProperty()
  p11_first_name        = db.StringProperty()
  p11_middle_initial    = db.StringProperty()
  p11_sex               = db.StringProperty()
  p11_birth_date        = db.StringProperty()
  p11_birth_month       = db.StringProperty()
  p11_birth_day         = db.StringProperty()
  p11_birth_year        = db.StringProperty()
  p11_hispanic          = db.StringProperty()
  p11_race              = db.StringProperty()
  p11_usual_residence   = db.StringProperty()
  p11_relation          = db.StringProperty()

class APIHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write('''
        this URL accepts POSTs only.  An email address and an API key are required.
    ''')

  def post(self):
    # try to have some semblance of security.  Require an API key
    api_key = self.request.get('api_key', default_value=None)
    if api_key is None or api_key != shared_secrety_api_key:
        self.response.out.write('''A valid 'api_key' is required: "''' + api_key + '"')
        return

    # we were given an email, try to get the entry associated with it
    email   = self.request.get('email', default_value=None)
    if email is None or len(email) == 0:
        self.response.out.write(''''email' is required: "''' + email + '"')
        return

    unique_key   = self.request.get('unique_key', default_value="mailto:")
    unique_key   = '%s%s' % (unique_key, email)

    properties = [
        'email',
        'phone',
        'address',
        'address_ownership',
        'streetaddress',
        'streetaddress2',
        'city',
        'state',
        'zip',
        'ownership',
        'num_residents',
        'unique_key',
    ]

    person_properties = [
        'last_name',
        'first_name',
        'middle_initial',
        'sex',
        'birth_date',
        'birth_month',
        'birth_day',
        'birth_year',
        'hispanic',
        'race',
        'usual_residence',
        'relation',
    ]

    # build a dict of valid properties
    valid_properties = {}
    for num_person in range(12):
        for property in person_properties:
            valid_properties['p%02d_%s' % (num_person, property)] = 1

    for property in properties:
        valid_properties[property] = 1

    entry_dict = {}
    for prop_name, prop_class in Entry.properties().iteritems():
        if prop_name in valid_properties:
            value = self.request.get(prop_name, default_value=None)
            if value:
                entry_dict[prop_name] = value

    entry_dict['unique_key'] = unique_key

    # save the entry
    entry = Entry(key_name=unique_key, **entry_dict)
    entry.put()

    self.response.out.write("<html><body><pre>")
    self.response.out.write("Entry saved: " + json.dumps(entry_dict, sort_keys = True, indent = 4) + "\n")
    self.response.out.write("Valid properties: " + json.dumps(valid_properties, sort_keys = True, indent = 4))
    self.response.out.write("<pre></body></html>")

class WizardHandler(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if not user:
      self.redirect(users.create_login_url(self.request.uri))

    persons     = []
    for num in range(0, 12):
      persons.append({ 'id': "%02d" % (num), 'next': "%02d" % (num + 1) });


    values = {
      'persons'    : persons,
      'logout_url' : users.create_logout_url(self.request.uri)
    }

    directory = os.path.dirname(__file__)
    path = os.path.join(directory, os.path.join('templates', 'wizard.html'))
    self.response.out.write(template.render(path, values))

  def post(self):
    user = users.get_current_user()
    if not user:
      self.redirect(users.create_login_url(self.request.uri))

    # we were given an email, try to get the entry associated with it
    email   = user.email()
    unique_key   = '%s%s' % ('00000', email)

    properties = [
        'first_name',
        'last_name',
        'email',
        'phone',
        'address',
        'address_ownership',
        'streetaddress',
        'streetaddress2',
        'city',
        'state',
        'zip',
        'ownership',
        'num_residents',
        'unique_key',
    ]

    person_properties = [
        'last_name',
        'first_name',
        'middle_initial',
        'sex',
        'birth_date',
        'birth_month',
        'birth_day',
        'birth_year',
        'hispanic',
        'race',
        'usual_residence',
        'relation',
    ]

    # build a dict of valid properties
    valid_properties = {}
    for num_person in range(12):
        for property in person_properties:
            valid_properties['p%02d_%s' % (num_person, property)] = 1

    for property in properties:
        valid_properties[property] = 1

    entry_dict = {}
    for prop_name, prop_class in Entry.properties().iteritems():
        if prop_name in valid_properties:
            value = self.request.get(prop_name, default_value=None)
            if value:
                entry_dict[prop_name] = value

    entry_dict['unique_key'] = unique_key
    entry_dict['email']      = user.email()

    # save the entry
    entry = Entry(key_name=unique_key, **entry_dict)
    entry.put()

    values = {
      'logout_url' : users.create_logout_url(self.request.uri),
      'entry_dict' : entry_dict,
    }

    directory = os.path.dirname(__file__)
    path = os.path.join(directory, os.path.join('templates', 'wizard_saved.html'))
    self.response.out.write(template.render(path, values))


application = webapp.WSGIApplication(
    [
      ('/api', APIHandler),
      ('/wizard', WizardHandler),
    ],
    debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
