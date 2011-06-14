#!/usr/bin/env python
#
# Participants Editor - DEI-FCTUC IHC 2011 
#	
# Developers:
#	- Renato Rodrigues
#	- Rui Molar
#
from models import *
from feedback import *
from contacts import *
from partners import *
from providers import *
from consumers import *
from xmlgenerator import *
from organizations import *
from datetime import datetime
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

#mainURL="http://participantseditor.appspot.com/"
mainURL="http://localhost:8080"

class MainHandler(webapp.RequestHandler):
	def get(self):
		self.response.out.write(template.render('templates/index.html',{}))

application = webapp.WSGIApplication([
	('/', MainHandler),
	
	('/providers',Providers),
	('/addproviders',AddProviders),
	('/editproviders',EditProviders),
	('/updateproviders',UpdateProviders),
	('/deleteproviders',DeleteProviders),
	
	('/consumers',Consumers),
	('/addconsumers',AddConsumers),
	('/editconsumers',EditConsumers),
	('/updateconsumers',UpdateConsumers),
	('/deleteconsumers',DeleteConsumers),
	
	('/partners',Partners),
	('/addpartners',AddPartners),
	('/editpartners',EditPartners),
	('/updatepartners',UpdatePartners),
	('/deletepartners',DeletePartners),
	
	('/organizations',Organizations),
	('/addorg',AddOrganizations),
	('/editorganizations',EditOrganizations),
	('/updateorganizations',UpdateOrganizations),
	('/deleteorganizations',DeleteOrganizations),
	
	('/contacts',Contacts),
	('/addcontact',AddContact),
	('/editcontacts',EditContacts),
	('/updatecontacts',UpdateContacts),
	('/deletecontacts',DeleteContacts),
	
	('/feedback',Feedback),
	('/dofeedback',DoFeedback),
	
	('/xml',XmlGenerator)
	],debug=True)

def main():
	util.run_wsgi_app(application)

if __name__ == '__main__':
	main()
