#!/usr/bin/env python
#
# Participants Editor - DEI-FCTUC IHC 2011 
#	
# Developers:
#	- Renato Rodrigues
#	- Rui Molar
#
from models import *
from xml.dom.minidom import Document
from google.appengine.ext import webapp

def createPartnersXml(self):
	#Get Consumers from DB
		partners = Partner.all().order('partner_name')
		
		#Start create XML file
		doc = Document()
		#Create Root
		root = doc.createElement("ListPartners")
		doc.appendChild(root)

		#Populate XML file
		for tempPartner in partners:
			#Create XML Elements
			partner = doc.createElement("partner") 
			partner.setAttribute("key",str(tempPartner.key()))
			root.appendChild(partner)
			
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
