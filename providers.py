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
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

#mainURL="http://participantseditor.appspot.com/"
mainURL="http://localhost:8080"

class Providers(webapp.RequestHandler):
	def get(self):
		self.response.out.write(
				template.render('templates/providers.html',
				{
					"organizations": Organization.all().order('name'),
					"contacts": Contact.all().order('first_name'),
				})
			)
	
class AddProviders(webapp.RequestHandler):
	def post(self):
		try:
			provider = Provider(
				provider_key = self.request.get('providerkey'),
				provider_name = self.request.get('providername'),
				organization = self.request.get('org'),
				contact_person = self.request.get('contact'),
				description = self.request.get('udescriptiontext')
			)
			provider.put()
			#self.response.out.write('{"status": "ok", "key":"'+ str(provider.key()) + '"}')
			self.redirect(mainURL);
		except Exception, e:
			self.response.out.write("{'status': 'fail' ,'reason':'"+str(e)+"' } ")

class EditProviders(webapp.RequestHandler):
   def get(self):
		try:
			providers=Provider.all().order('provider_name')
			if providers.count() > 0:
				self.response.out.write(
					template.render('templates/editproviders.html',
					{
						"providers": providers,
						"edit": "no",
					})
				)
			else:
				self.response.out.write(
					template.render('templates/editproviders.html',
					{
						"erro": "noresults",
						"edit": "no",
					})
				)
		except Exception, e:
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')

   def post(self):
		provider_key = self.request.get("prov")
		#self.response.out.write(provider_key)
		provider = Provider.get(provider_key)
		self.response.out.write(
					template.render('templates/editproviders.html',
					{
						"organizations": Organization.all().order('name'),
						"contacts": Contact.all().order('first_name'),
						"providers": Provider.all().order('provider_name'),
						"edit": "yes",
						"provider": provider,
					})
				)

class UpdateProviders(webapp.RequestHandler):
	def post(self):
		try:
			provider = Provider.get(self.request.get('key'))
			provider.provider_key = self.request.get('providerkey')
			provider.provider_name = self.request.get('providername')
			provider.organization = self.request.get('org')
			provider.contact_person = self.request.get('contact')
			provider.description = self.request.get('udescriptiontex')
			provider.timestamp = datetime.today() # now saves the last update
			provider.put()
			#self.response.out.write('{"status": "ok"}')
			self.redirect(mainURL);
		except Exception, e:
			#self.response.out.write(self.request.get('providerkey'))
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')

class DeleteProviders(webapp.RequestHandler):
    def get(self):
		try:
			provider = Provider.get(self.request.get('key'))
			provider.delete()
			#self.response.out.write('{"status": "ok"}')
			self.redirect(mainURL);
		except Exception, e:
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')
