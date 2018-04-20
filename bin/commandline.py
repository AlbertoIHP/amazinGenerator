from subprocess import call
import json
import io
import os
from componentparser import ComponentParser
from projectparser import ProjectParser

class CommandLine(object):

	def __init__(self):
		self.componentCreator = ComponentParser()
		self.projectCreator = ProjectParser()
		jsonFile = self.checkJsonConfFile()
		if( jsonFile == False ):
			self.data = self.createJsonConfFile()
		else:
			self.data = jsonFile


		


	def replaceJson(self):
		os.remove("./share/conf.json")
		with open( './share/conf.json', 'w' ) as outfile:
			json.dump( self.data, outfile )


	def execute(self, command):

		command = command.split('-')


		if( command[0] == 'help'):
			self.displayHelp()

		elif( command[0] == 'new project ' and len( command ) == 2 ):
			self.projectCreator.generateProject( command[1], self )

		elif( command[0] == 'show projects' and len( command ) == 1 ):
			self.projectCreator.showProjects( self )

		elif( command[0] == 'del project ' and len( command ) == 2 ):
			self.projectCreator.deleteProject( str( command[1], self ) )

		elif( command[0] == 'use project ' and len( command ) == 2 ):
			self.projectCreator.useProject( str( command[1] ), self )

		elif( command[0] == 'new component ' and len( command ) == 2 ):
			self.componentCreator.createComponent( self.data['currentProject'], str( command[1]), self )

		elif( command[0] == 'show components' and len( command ) == 1 ):
			print 'se deben mostrar todos los componentes del proyecto cargado'

		elif( command[0] == 'del component ' and len( command ) == 2 ):
			print 'se debe eliminar el componente'+str( command[1] )

		elif( command[0] == 'use component ' and len( command ) == 2 ):
			print 'se debe usar el componente'+str( command[1] )

		elif( command[0] == 'clear'):
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
		print 'General Commands:'
		print '-----------------'
		print 'exit (This will close amazinGenerator)'
		print '																				  '
		print '																				  '
		print 'Project Commands:'
		print '-----------------'
		print 'new project -projectname (This will create a new react native project)'
		print 'show projects (This will show your current projects)'
		print 'del project -projectname (This will delete your project)'
		print 'use project -projectname (This will load your project for create components)'
		print '																				  '
		print '																				  '
		print 'Components Commands:'
		print '--------------------'
		print 'new component -componentname (This will create a component inside your loaded project)'
		print 'del component -componentname (This will delete the component)'
		print 'show components (This will show the whole list of components of loaded project)'
		print 'use component -componentname (This will load your component for configurate it)'


