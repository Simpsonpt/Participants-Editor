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

def createProvidersXml(self):
		#Get Providers from DB
		providers = Provider.all().order('provider_name')
		
		#Start create XML file
		doc = Document()
		#Create Root
		root = doc.createElement("ListProviders")
		doc.appendChild(root)

		#Populate XML file
		for tempProvider in providers:
			#Create XML Elements
			provider = doc.createElement("provider") 
			provider.setAttribute("key",str(tempProvider.key()))
			root.appendChild(provider)
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
			
		#Print/Send XML file
		#print doc.toprettyxml(indent="  ")
		self.response.headers["Content-Type"] = "application/xml"
		self.response.out.write(doc.toprettyxml(indent="  "))
