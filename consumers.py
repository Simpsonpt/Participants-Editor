#!/usr/bin/env python
#
# Participants Editor - DEI-FCTUC IHC 2011 
#	
# Developers:
#	- Renato Rodrigues
#	- Rui Molar
#
from models import *
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

#mainURL="http://participantseditor.appspot.com/"
mainURL="http://localhost:8080"

class Consumers(webapp.RequestHandler):
	def get(self):
		self.response.out.write(
				template.render('templates/consumers.html',{}))
	
class AddConsumers(webapp.RequestHandler):
	def post(self):
		try:
			consumer = Consumer(
				profile_name = self.request.get('profilename'),
				problem_definition = self.request.get('problemdefinition'),
				goal_definition = self.request.get('goaldefinition'),
				description = self.request.get('udescriptiontex')
			)
			consumer.put()
			#self.response.out.write('{"status": "ok", "key":"'+ str(consumer.key()) + '"}')
			self.redirect(mainURL);
		except Exception, e:
			self.response.out.write("{'status': 'fail' ,'reason':'"+str(e)+"' } ")

class EditConsumers(webapp.RequestHandler):
   def get(self):
		try:
			consumers=Consumer.all().order('profile_name')
			if consumers.count() > 0:
				self.response.out.write(
					template.render('templates/editconsumers.html',
					{
						"consumers": consumers,
						"edit": "no",
					})
				)
			else:
				self.response.out.write(
					template.render('templates/editconsumers.html',
					{
						"erro": "noresults",
						"edit": "no",
					})
				)
		except Exception, e:
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')

   def post(self):
		profile_key = self.request.get("prov")
		consumer = Consumer.get(profile_key)
		#self.response.out.write(consumer.description)
		self.response.out.write(
					template.render('templates/editconsumers.html',
					{
						"consumers": Consumer.all().order('profile_name'),
						"edit": "yes",
						"consumer": consumer,
					})
				)

class UpdateConsumers(webapp.RequestHandler):
	def post(self):
		try:
			consumer = Consumer.get(self.request.get('key'))
			consumer.profile_name = self.request.get('profilename')
			consumer.problem_definition = self.request.get('problemdefinition')
			consumer.goal_definition = self.request.get('goaldefinition')
			consumer.description = self.request.get('udescriptiontex')
			consumer.timestamp = datetime.today() # now saves the last update
			consumer.put()
			self.response.out.write('{"status": "ok"}')
			#self.redirect(mainURL);
		except Exception, e:
			#self.response.out.write(self.request.get('providerkey'))
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')

class DeleteConsumers(webapp.RequestHandler):
    def get(self):
		try:
			consumer = Consumer.get(self.request.get('key'))
			consumer.delete()
			#self.response.out.write('{"status": "ok"}')
			self.redirect(mainURL);
		except Exception, e:
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')
