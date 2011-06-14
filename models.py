#!/usr/bin/env python
#
# Participants Editor - DEI-FCTUC IHC 2011 
#	
# Developers:
#	- Renato Rodrigues
#	- Rui Molar
#
from google.appengine.ext import db
from google.appengine.api import users

#DB Model for Provider
class Provider(db.Model):
	provider_key = db.StringProperty(required=True)
	provider_name = db.StringProperty(required=True)
	organization = db.StringProperty(required=True)
	contact_person = db.StringProperty(required=True)
	description = db.StringProperty()
	timestamp = db.DateTimeProperty(auto_now_add=True)
	
#DB Model for Consumers
class Consumer(db.Model):
	profile_name = db.StringProperty(required=True)
	problem_definition = db.StringProperty(required=True)
	goal_definition = db.StringProperty(required=True)
	description = db.StringProperty()
	timestamp = db.DateTimeProperty(auto_now_add=True)

#DB Model for Partner
class Partner(db.Model):
	partner_key = db.StringProperty(required=True)
	partner_name = db.StringProperty(required=True)
	partner_type = db.StringProperty(required=True)
	organization = db.StringProperty(required=True)
	contact_person = db.StringProperty(required=True)
	description = db.StringProperty()
	timestamp = db.DateTimeProperty(auto_now_add=True)

#DB Model for Organizations
class Organization(db.Model):
	name = db.StringProperty(required=True)
	website = db.LinkProperty(required=True)
	address = db.StringProperty()
	street = db.StringProperty()
	post_code = db.StringProperty()
	city = db.StringProperty()
	state = db.StringProperty()
	country = db.StringProperty()
	timestamp = db.DateTimeProperty(auto_now_add=True)
	
#DB Model for Contacts
class Contact(db.Model):
	first_name = db.StringProperty(required=True)
	last_name = db.StringProperty(required=True)
	telephone = db.PhoneNumberProperty(required=True)
	email = db.EmailProperty(required=True)
	timestamp = db.DateTimeProperty(auto_now_add=True)
