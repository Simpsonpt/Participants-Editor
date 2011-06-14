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

class Organizations(webapp.RequestHandler):
	def get(self):
		self.response.out.write(
				template.render('templates/organizations.html',{}))

class AddOrganizations(webapp.RequestHandler):
	def post(self):
		try:
			org = Organization(
				name = self.request.get('orgname'),
				website = self.request.get('orgwebsite'),
				address = self.request.get('address'),
				street = self.request.get('street'),
				post_code = self.request.get('postcode'),
				city = self.request.get('city'),
				state = self.request.get('state'),
				country = self.request.get('country')
			)
			org.put()
			self.response.out.write('{"status": "ok", "key":"'+ str(org.key()) + '"}')
			self.redirect(mainURL);
		except Exception, e:
			self.response.out.write("{'status': 'fail' ,'reason':'"+str(e)+"' } ")

class EditOrganizations(webapp.RequestHandler):
   def get(self):
		try:
			organizations=Organization.all().order('name')
			if organizations.count() > 0:
				self.response.out.write(
					template.render('templates/editorganizations.html',
					{
						"organizations": organizations,
						"edit": "no",
					})
				)
			else:
				self.response.out.write(
					template.render('templates/editorganizations.html',
					{
						"erro": "noresults",
						"edit": "no",
					})
				)
		except Exception, e:
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')

   def post(self):
		org_key = self.request.get("prov")
		organization = Organization.get(org_key)
		#self.response.out.write(consumer.description)
		self.response.out.write(
					template.render('templates/editorganizations.html',
					{
						"organizations": Organization.all().order('name'),
						"edit": "yes",
						"organization": organization,
					})
				)

class UpdateOrganizations(webapp.RequestHandler):
	def post(self):
		try:
			organization = Organization.get(self.request.get('key'))
			organization.name = self.request.get('orgname')
			organization.website = self.request.get('orgwebsite')
			organization.address = self.request.get('address')
			organization.street = self.request.get('street')
			organization.post_code = self.request.get('postcode')
			organization.city = self.request.get('city')
			organization.state = self.request.get('state')
			organization.country = self.request.get('country')
			organization.timestamp = datetime.today() # now saves the last update
			organization.put()
			#self.response.out.write('{"status": "ok"}')
			self.redirect(mainURL);
		except Exception, e:
			#self.response.out.write(self.request.get('providerkey'))
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')

class DeleteOrganizations(webapp.RequestHandler):
    def get(self):
		try:
			organization = Organization.get(self.request.get('key'))
			organization.delete()
			#self.response.out.write('{"status": "ok"}')
			self.redirect(mainURL);
		except Exception, e:
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')
