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

def createConsumersXml(self):
		#Get Consumers from DB
		consumers = Consumer.all().order('profile_name')
		
		#Start create XML file
		doc = Document()
		#Create Root
		root = doc.createElement("ListConsumers")
		doc.appendChild(root)

		#Populate XML file
		for tempConsumer in consumers:
			#Create XML Elements
			consumer = doc.createElement("consumer") 
			consumer.setAttribute("key",str(tempConsumer.key()))
			root.appendChild(consumer)
			
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
			
		#Print/Send XML file
		#print doc.toprettyxml(indent="  ")
		self.response.headers["Content-Type"] = "application/xml"
		self.response.out.write(doc.toprettyxml(indent="  "))
