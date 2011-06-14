#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Participants Editor - DEI-FCTUC IHC 2011 
#	
# Developers:
#	- Diogo Balseiro
#	- Flavio Guilherme
#	- Renato Rodrigues
#	- Rui Molar
#
from models import *
from partnersxml import *
from providersxml import *
from consumersxml import *
from participantsxml import *
from xml.dom.minidom import Document
from google.appengine.ext import webapp

class XmlGenerator(webapp.RequestHandler):
	def get(self):
		kind=self.request.get('kind')
		if(kind=="providers"):
			createProvidersXml(self)
		elif(kind=="consumers"):
			createConsumersXml(self)
		elif(kind=="partners"):
			createPartnersXml(self)
		elif(kind=="participants"):
			createParticipantsXml(self)
