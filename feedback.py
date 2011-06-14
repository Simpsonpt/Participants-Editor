#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Participants Editor - DEI-FCTUC IHC 2011 
#   
# Developers:
#   - Diogo Balseiro
#   - Flavio Guilherme
#   - Renato Rodrigues
#   - Rui Molar
#
from models import *
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class Feedback(webapp.RequestHandler):
	def get(self):
		try:
			providers=Provider.all().order('provider_name')
			if providers.count() > 0:
				self.response.out.write(
					template.render('templates/feedback.html',
					{
						"providers": providers,
						"edit": "no",
						"list": "check", 
					})
				)
			else:
				self.response.out.write(
					template.render('templates/feedback.html',
					{
						"erro": "noresults",
						"edit": "no",
					})
				)
		except Exception, e:
			self.response.out.write('{"status": "fail","reason":"'+str(e)+'"}')
			
class DoFeedback(webapp.RequestHandler):
   def post(self):
		provider_key = self.request.get("prov")
		#self.response.out.write(provider_key)
		provider = Provider.get(provider_key)
		self.response.out.write(
					template.render('templates/feedback.html',
					{
						"providers": Provider.all().order('provider_name'),
						"edit": "yes",
						"list": "nocheck",
						"provider": provider,
					})
				)
