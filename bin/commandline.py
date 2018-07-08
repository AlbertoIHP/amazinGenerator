from subprocess import call
import json
import io
import os
from componentparser import ComponentParser
from projectparser import ProjectParser
from tabparser import TabParser
import re


class CommandLine(object):

	def __init__(self):
		self.componentCreator = ComponentParser()
		self.projectCreator = ProjectParser()
		self.tabCreator = TabCreator()
		jsonFile = self.checkJsonConfFile()
		if( jsonFile == False ):
			self.data = self.createJsonConfFile()
		else:
			self.data = jsonFile


		


	def replaceJson(self):
		os.remove("./share/conf.json")
		with open( './share/conf.json', 'w' ) as outfile:
			json.dump( self.data, outfile )



	def hasTemplate(self, command):
		template = re.search('(?<=--template=)[A-Za-z_.]*', command)
		name = re.search('(?<=--name=)[A-Za-z_.]*',command)
	
		if( template and name ):
			template = str( template.group(0) )
			name = str( name.group(0) )
			return { 'name': name, 'template': template}
		elif( name ):
			name = str( name.group(0) )
			return { 'name': name, 'template': False}
		else:
			return False	





	def execute(self, command):

		if( re.search('(help)*', command).group(0) ):
			self.displayHelp()




		elif( re.search('(new project)*', command).group(0) ):
			res = self.hasTemplate( command )
			if( res and res['template']):
				a = '5'
				#Call template builder
			elif( res ):
				self.projectCreator.generateProject( res['name'], self )
			else:
				print "You have to specify a name to build a new project"
				

		
		elif( re.search('(show projects)*', command).group(0) ):
			self.projectCreator.showProjects( self )




		elif( re.search('(del project)*', command).group(0) ):
			if( self.hasTemplate( command ) ):
				self.projectCreator.useProject( self.hasTemplate( command )['name'], self )
				self.projectCreator.deleteProject( self.hasTemplate( command )['name'], self )
			else:
				print "You have to specify a name to delete the project"	




		elif( re.search('(use project)*', command).group(0) ):
			if( self.hasTemplate( command ) ):
				self.projectCreator.useProject( self.hasTemplate( command )['name'], self )
			else:
				print "You have to specify a name to use the project"	


			

		elif( re.search('(new component)*', command).group(0) ):
			res = self.hasTemplate( command )
			if( res and res['template']):
				a = '5'
				#Call template builder
			elif( res ):
				self.componentCreator.createComponent( self.data['currentProject'], res['name'], self )
			else:
				print "You have to specify a name to build a new component"


		elif( re.search('(new tab)*', command).group(0) ):
			res = self.hasTemplate( command )
			if( res and res['template']):
				a = '5'
				#Call template builder
			elif( res ):
				self.componentCreator.createComponent( self.data['currentProject'], res['name'], self )
				self.tabCreator.createTab( self.data['currentProject'], res['name'], self )
			else:
				print "You have to specify a name to build a new component"

				

		elif( re.search('(show components)*', command).group(0) ):
			print 'se deben mostrar todos los componentes del proyecto cargado'

		elif( re.search('(del component)*', command).group(0) ):
			print 'se debe eliminar el componente'+str( command[1] )

		elif( re.search('(use component)*', command).group(0) ):
			print 'se debe usar el componente'+str( command[1] )

		elif( re.search('(clear)*', command).group(0) ):
			self.runCommand('clear')

		else:
			print "We could not recognize the command..."
			self.displayHelp()	






	def createJsonConfFile( self ):
		print 'Creating JSON conf file...'
		data = {}
		data['projects'] = []
		data['currentProject'] = ''
		data['currentComponent'] = ''

		with open( './share/conf.json', 'w' ) as outfile:
			json.dump( data, outfile )
		print 'JSON conf file created succesfully...'
		return data




	def checkJsonConfFile( self ):
		print 'Checking for an existing JSON conf file...'
		try:
			with open( './share/conf.json' ) as json_file:
				print 'Founded, loading...'
				return json.load( json_file )
		except IOError:
			print 'Not founded...'
			return False


	def runCommand( self, command ):
		command = command.split(' ')
		call(command)


	def displayHelp( self ):
		print
		print
		print 'General Commands:'
		print '-----------------'
		print 'exit (This will close amazinGenerator)'
		print 
		print 
		print 'Project Commands:'
		print '-----------------'
		print 'new project --name=projectname --template=templatename (This will create a new react native project)'
		print 'show projects (This will show your current projects)'
		print 'del project --name=projectname (This will delete your project)'
		print 'use project --name=projectname (This will load your project for create components)'
		print 
		print 
		print 'Components Commands:'
		print '--------------------'
		print 'new component --name=componentname --template=templatename (This will create a component inside your loaded project)'
		print 'del component --name=componentname  (This will delete the component)'
		print 'show components (This will show the whole list of components of loaded project)'
		print 'use component --name=componentname (This will load your component for configurate it)'
		print 
		print 
		print 'Tabs Commands:'
		print '--------------------'
		print 'new tab --name=tabname --template=templatename (This will create a tab inside your maincomponent)'
		print
		print


