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

class Partners(webapp.RequestHandler):
	def get(self):
		self.response.out.write(
				template.render('templates/partners.html',
				{
					"organizations": Organization.all().order('name'),
					"contacts": Contact.all().order('first_name'),
				})
			)
	
class AddPartners(webapp.RequestHandler):
	def post(self):
		try:
			partner = Partner(
				partner_key = self.request.get('partnerkey'),
				partner_name = self.request.get('partnername'),
				partner_type = self.request.get('partnertype'),
				organization = self.request.get('org'),
				contact_person = self.request.get('contact'),
				description = self.request.get('udescriptiontext')
			)
			partner.put()
			self.response.out.write('{"status": "ok", "key":"'+ str(partner.key()) + '"}')
			self.redirect(mainURL);
		except Exception, e:
			self.response.out.write("{'status': 'fail' ,'reason':'"+str(e)+"' } ")

class EditPartners(webapp.RequestHandler):
   def get(self):
		try:
			partners=Partner.all().order('partner_name')
			if partners.count() > 0:
				self.response.out.write(
					template.render('templates/editpartners.html',
					{
						"partners": partners,
						"edit": "no",
					})
				)
			else:
				self.response.out.write(
					template.render('templates/editpartners.html',
					{
						"erro": "noresults",
						"edit": "no",
					})
				)
		except Exception, e:
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')

   def post(self):
		partner_key = self.request.get("prov")
		partner = Partner.get(partner_key)
		#self.response.out.write(consumer.description)
		self.response.out.write(
					template.render('templates/editpartners.html',
					{
						"organizations": Organization.all().order('name'),
						"contacts": Contact.all().order('first_name'),
						"partners": Partner.all().order('partner_name'),
						"edit": "yes",
						"partner": partner,
					})
				)

class UpdatePartners(webapp.RequestHandler):
	def post(self):
		try:
			partner = Partner.get(self.request.get('key'))
			partner.partner_name = self.request.get('partnername')
			partner.partner_type = self.request.get('partnertype')
			partner.organization = self.request.get('org')
			partner.contact_person = self.request.get('contact')
			partner.description = self.request.get('udescriptiontex')
			partner.timestamp = datetime.today() # now saves the last update
			partner.put()
			self.response.out.write('{"status": "ok"}')
			#self.redirect(mainURL);
		except Exception, e:
			#self.response.out.write(self.request.get('providerkey'))
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')

class DeletePartners(webapp.RequestHandler):
    def get(self):
		try:
			partner = Partner.get(self.request.get('key'))
			partner.delete()
			#self.response.out.write('{"status": "ok"}')
			self.redirect(mainURL);
		except Exception, e:
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')
