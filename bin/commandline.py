from subprocess import call
import json
import io
import os

class CommandLine(object):

	def __init__(self):
		jsonFile = self.checkJsonConfFile()
		if( jsonFile == False ):
			self.data = self.createJsonConfFile()
		else:
			self.data = jsonFile



	def generateProject(self, projectName):
		print 'Checking if Node and npm are installed'
		try:
			self.runCommand('npm -v')
			print 'succesfully'

			print 'installing react native CLI'
			self.runCommand('npm install -g create-react-native-app')
			print 'succesfully'

			print 'creating project: '+str( projectName )
			self.runCommand( 'create-react-native-app projects/'+str( projectName ) )
			print 'succesfully'

			print 'adding your project into JSON conf file'
			newProject = {'name' : projectName , 'components': [], 'services': [], 'routes': [] }
			self.data['projects'].append( newProject )
			self.replaceJson()
			print 'succesfully'

			print 'Moving and checking directory work'
			os.chdir( 'projects/'+str( projectName ) )
			print os.getcwd()

			print 'Installing axios for fetching'
			self.runCommand('npm install axios --save')
			print 'succesfully'

			print 'Installing react-native-router-flux for routing system'
			self.runCommand('npm install react-native-router-flux --save')
			print 'succesfully'

			print 'Installing native-base for styling css'
			self.runCommand('npm install native-base --save')
			print 'succesfully'

			print 'Installing socket for events configuration (real time apps)'
			self.runCommand('npm install socket.io-client --save')
			print 'succesfully'

			print 'Doing some amazinGenerator magic...'
			self.runCommand('rm -rf App.test.js')
			self.runCommand('rm -rf App.js')
			self.runCommand('cp ../../share/App.template App.js')
			self.runCommand('mkdir src')
			os.chdir( 'src' )
			self.runCommand('mkdir Services')
			self.runCommand('mkdir Components')
			self.runCommand('mkdir Routes')
			self.runCommand('cp ../../../share/base.template Services/base.js')
			self.runCommand('cp ../../../share/routes.template Routes/index.js')
			self.runCommand('cp ../../../share/index.template index.js')
			os.chdir('../../../')
			print 'succesfully'
			print 'Now by using your project you can create components, services, etc.'

		except OSError:
			print "Error: You have not installed NPM, please install it before continue..."
			
		


	def replaceJson(self):
		os.remove("./share/conf.json")
		with open( './share/conf.json', 'w' ) as outfile:
			json.dump( self.data, outfile )

	def execute(self, command):

		command = command.split('-')


		if( command[0] == 'help'):
			self.displayHelp()
		elif( command[0] == 'new project ' and len( command ) == 2 ):
			self.generateProject( command[1] )
		elif( command[0] == 'show projects' and len( command ) == 1 ):
			self.showProjects()
		elif( command[0] == 'del project ' and len( command ) == 2 ):
			self.deleteProject( str( command[1] ) )
		elif( command[0] == 'use project ' and len( command ) == 2):
			self.useProject( str( command[1] ) )
		elif( command[0] == 'new component ' and len( command ) == 2 ):
			print 'se debe crear componente '+str(command[1])
		elif( command[0] == 'show components' and len( command ) == 1 ):
			print 'se deben mostrar todos los componentes del proyecto cargado'
		elif( command[0] == 'del component ' and len( command ) == 2 ):
			print 'se debe eliminar el componente'+str(command[1])
		elif( command[0] == 'use component ' and len( command ) == 2):
			print 'se debe usar el componente'+str(command[1])
		elif( command[0] == 'clear'):
			self.runCommand('clear')
		else:
			print "We could not recognize the command..."
			self.displayHelp()	




	def deleteProject( self, projectName ):
		print 'Deleting project '+str( projectName )
		self.runCommand( 'rm -rf projects/'+str( projectName ) )
		if( self.data['currentProject'] == str( projectName ) ):
			self.data['currentProject'] = ''
			self.replaceJson()

		for project in self.data['projects']:
			if( project['name'] == str( projectName ) ):
				self.data['projects'].remove( project )
				self.replaceJson()
				break

		print 'succesfully'

	def useProject( self, projectName ):
		self.data['currentProject'] = projectName
		self.replaceJson()

	def showProjects( self ):
		for project in self.data['projects']:
			print "- "+str( project['name'] )


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


