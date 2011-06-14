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

class Contacts(webapp.RequestHandler):
	def get(self):
		self.response.out.write(
				template.render('templates/contacts.html',{}))

class AddContact(webapp.RequestHandler):
	def post(self):
		try:
			contact = Contact(
				first_name = self.request.get('firstname'),
				last_name = self.request.get('lastname'),
				telephone = self.request.get('phone'),
				email = self.request.get('email'),
			)
			contact.put()
			self.response.out.write('{"status": "ok", "key":"'+ str(contact.key()) + '"}')
			self.redirect(mainURL);
		except Exception, e:
			self.response.out.write("{'status': 'fail' ,'reason':'"+str(e)+"' } ")

class EditContacts(webapp.RequestHandler):
   def get(self):
		try:
			contacts=Contact.all().order('first_name')
			if contacts.count() > 0:
				self.response.out.write(
					template.render('templates/editcontacts.html',
					{
						"contacts": contacts,
						"edit": "no",
					})
				)
			else:
				self.response.out.write(
					template.render('templates/editcontacts.html',
					{
						"erro": "noresults",
						"edit": "no",
					})
				)
		except Exception, e:
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')

   def post(self):
		contact_key = self.request.get("prov")
		contact = Contact.get(contact_key)
		#self.response.out.write(consumer.description)
		self.response.out.write(
					template.render('templates/editcontacts.html',
					{
						"contacts": Contact.all().order('first_name'),
						"edit": "yes",
						"contact": contact,
					})
				)

class UpdateContacts(webapp.RequestHandler):
	def post(self):
		try:
			contact = Contact.get(self.request.get('key'))
			contact.first_name = self.request.get('firstname')
			contact.last_name = self.request.get('lastname')
			contact.telephone = self.request.get('phone')
			contact.email = self.request.get('email')
			contact.timestamp = datetime.today() # now saves the last update
			contact.put()
			#self.response.out.write('{"status": "ok"}')
			self.redirect(mainURL);
		except Exception, e:
			#self.response.out.write(self.request.get('providerkey'))
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')

class DeleteContacts(webapp.RequestHandler):
    def get(self):
		try:
			contact = Contact.get(self.request.get('key'))
			contact.delete()
			#self.response.out.write('{"status": "ok"}')
			self.redirect(mainURL);
		except Exception, e:
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')
