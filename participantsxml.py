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
from xml.dom.minidom import Document
from google.appengine.ext import webapp

def createParticipantsXml(self):
		#Get Participants from DB
		providers = Provider.all().order('provider_name')
		consumers = Consumer.all().order('profile_name')
		partners = Partner.all().order('partner_name')
		
		#Start create XML file
		doc = Document()
		#Create Root
		root = doc.createElement("Participants")
		doc.appendChild(root)
		
		#List of Providers
		listProvider = doc.createElement("Providers")
		root.appendChild(listProvider)
		
		#Populate XML file
		for tempProvider in providers:
			#Create XML Elements
			provider = doc.createElement("provider") 
			provider.setAttribute("key",str(tempProvider.key()))
			listProvider.appendChild(provider)
			providerKey = doc.createElement("providerKey")
			providerName = doc.createElement("providerName")
			organizationField = doc.createElement("organization")
			name = doc.createElement("name")
			www = doc.createElement("www")
			address = doc.createElement("address")
			street = doc.createElement("street")
			postcode = doc.createElement("postcode")
			city = doc.createElement("city")
			state = doc.createElement("state")
			country = doc.createElement("country")
			contactPerson = doc.createElement("contactPerson")
			contactName = doc.createElement("contactName")
			contactPhone = doc.createElement("contactPhone")
			contactEmail = doc.createElement("contactEmail")
			description = doc.createElement("description")
			#Structure of XML File
			provider.appendChild(providerKey)
			provider.appendChild(providerName)
			provider.appendChild(organizationField)
			organizationField.appendChild(name)
			organizationField.appendChild(www)
			organizationField.appendChild(address)		
			address.appendChild(street)
			address.appendChild(postcode)
			address.appendChild(city)
			address.appendChild(state)
			address.appendChild(country)		
			provider.appendChild(contactPerson)	
			contactPerson.appendChild(contactName)
			contactPerson.appendChild(contactPhone)
			contactPerson.appendChild(contactEmail)		
			provider.appendChild(description)
			
			#Get Provider Key
			key=doc.createTextNode(tempProvider.provider_key)
			providerKey.appendChild(key)
			#Get Provider Name
			pname=doc.createTextNode(tempProvider.provider_name)
			providerName.appendChild(pname)
			#Get Organization
			org=doc.createTextNode(tempProvider.organization)
			name.appendChild(org)
			
			#Get More Info About Organization
			tempOrg = Organization.all().filter('name = ',tempProvider.organization).get()
			txt = doc.createTextNode(tempOrg.website)
			www.appendChild(txt)
			#Address
			tempStreet = doc.createTextNode(tempOrg.street)
			street.appendChild(tempStreet)
			tempPostcode = doc.createTextNode(tempOrg.post_code)
			postcode.appendChild(tempPostcode)
			tempCity = doc.createTextNode(tempOrg.city)
			city.appendChild(tempCity)
			tempState = doc.createTextNode(tempOrg.state)
			state.appendChild(tempState)
			tempCountry = doc.createTextNode(tempOrg.country)
			country.appendChild(tempCountry)
			
			#Get More Info About Contact
			div=tempProvider.contact_person.split(" ")
			firstName=div[0]
			lastName=div[1]
			tempContact = Contact.all()
			tempContact.filter('first_name = ',firstName)
			tempContact.filter('last_name = ',lastName)
			tempContact=tempContact.get()
			
			tempName = doc.createTextNode(tempProvider.contact_person)
			contactName.appendChild(tempName)
			tempPhone = doc.createTextNode(tempContact.telephone)
			contactPhone.appendChild(tempPhone)
			tempEmail = doc.createTextNode(tempContact.email)
			contactEmail.appendChild(tempEmail)		
			
			desc = doc.createTextNode(tempProvider.description)
			description.appendChild(desc)	
		
		#List Consumers
		listConsumer = doc.createElement("Consumers")
		root.appendChild(listConsumer)

		#Populate XML file
		for tempConsumer in consumers:
			#Create XML Elements
			consumer = doc.createElement("consumer") 
			consumer.setAttribute("key",str(tempConsumer.key()))
			listConsumer.appendChild(consumer)
			
			profileName = doc.createElement("profileName")
			problemDefinition = doc.createElement("problemDefinition")
			goalDefinition = doc.createElement("goalDefinition")
			description = doc.createElement("description")
			
			#Structure of XML File
			consumer.appendChild(profileName)
			consumer.appendChild(problemDefinition)
			consumer.appendChild(goalDefinition)	
			consumer.appendChild(description)
						
			#Get Consumer Name
			name=doc.createTextNode(tempConsumer.profile_name)
			profileName.appendChild(name)
			#Get Problem Definition
			pd=doc.createTextNode(tempConsumer.problem_definition)
			problemDefinition.appendChild(pd)
			#Get Goal Definition
			gd=doc.createTextNode(tempConsumer.goal_definition)
			goalDefinition.appendChild(gd)
			#Get Description			
			desc = doc.createTextNode(tempConsumer.description)
			description.appendChild(desc)	
		
		#List Partners
		listPartners = doc.createElement("Partners")
		root.appendChild(listPartners)

		#Populate XML file
		for tempPartner in partners:
			#Create XML Elements
			partner = doc.createElement("partner") 
			partner.setAttribute("key",str(tempPartner.key()))
			listPartners.appendChild(partner)
			
			partnerKey = doc.createElement("partnerKey")
			partnerName = doc.createElement("partnerName")
			partnerType = doc.createElement("partnerType")
			organizationField = doc.createElement("organization")
			name = doc.createElement("name")
			www = doc.createElement("www")
			address = doc.createElement("address")
			street = doc.createElement("street")
			postcode = doc.createElement("postcode")
			city = doc.createElement("city")
			state = doc.createElement("state")
			country = doc.createElement("country")
			contactPerson = doc.createElement("contactPerson")
			contactName = doc.createElement("contactName")
			contactPhone = doc.createElement("contactPhone")
			contactEmail = doc.createElement("contactEmail")
			description = doc.createElement("description")
			#Structure of XML File
			partner.appendChild(partnerKey)
			partner.appendChild(partnerName)
			partner.appendChild(partnerType)
			partner.appendChild(organizationField)
			organizationField.appendChild(name)
			organizationField.appendChild(www)
			organizationField.appendChild(address)		
			address.appendChild(street)
			address.appendChild(postcode)
			address.appendChild(city)
			address.appendChild(state)
			address.appendChild(country)		
			partner.appendChild(contactPerson)	
			contactPerson.appendChild(contactName)
			contactPerson.appendChild(contactPhone)
			contactPerson.appendChild(contactEmail)		
			partner.appendChild(description)
			
			#Get Partner Key
			key=doc.createTextNode(tempPartner.partner_key)
			partnerKey.appendChild(key)
			#Get Partner Name
			pname=doc.createTextNode(tempPartner.partner_name)
			partnerName.appendChild(pname)
			#Get Partner Type
			ptype=doc.createTextNode(tempPartner.partner_type)
			partnerType.appendChild(ptype)
			#Get Organization
			org=doc.createTextNode(tempPartner.organization)
			name.appendChild(org)
			
			#Get More Info About Organization
			tempOrg = Organization.all().filter('name = ',tempPartner.organization).get()
			txt = doc.createTextNode(tempOrg.website)
			www.appendChild(txt)
			#Address
			tempStreet = doc.createTextNode(tempOrg.street)
			street.appendChild(tempStreet)
			tempPostcode = doc.createTextNode(tempOrg.post_code)
			postcode.appendChild(tempPostcode)
			tempCity = doc.createTextNode(tempOrg.city)
			city.appendChild(tempCity)
			tempState = doc.createTextNode(tempOrg.state)
			state.appendChild(tempState)
			tempCountry = doc.createTextNode(tempOrg.country)
			country.appendChild(tempCountry)
			
			#Get More Info About Contact
			div=tempPartner.contact_person.split(" ")
			firstName=div[0]
			lastName=div[1]
			tempContact = Contact.all()
			tempContact.filter('first_name = ',firstName)
			tempContact.filter('last_name = ',lastName)
			tempContact=tempContact.get()
			
			tempName = doc.createTextNode(tempPartner.contact_person)
			contactName.appendChild(tempName)
			tempPhone = doc.createTextNode(tempContact.telephone)
			contactPhone.appendChild(tempPhone)
			tempEmail = doc.createTextNode(tempContact.email)
			contactEmail.appendChild(tempEmail)		
			
			desc = doc.createTextNode(tempPartner.description)
			description.appendChild(desc)	
		
		
		#Print/Send XML file
		#print doc.toprettyxml(indent="  ")
		self.response.headers["Content-Type"] = "application/xml"
		self.response.out.write(doc.toprettyxml(indent="  "))		
