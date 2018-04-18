from subprocess import call
import json
import io
import os


class ProjectParser(object):



	def showProjects( self, console ):
		for project in console.data['projects']:
			print "- "+str( project['name'] )



	def useProject( self, projectName, console ):
		console.data['currentProject'] = projectName
		console.replaceJson()



	def deleteProject( self, projectName, console ):
		print 'Deleting project '+str( projectName )
		console.runCommand( 'rm -rf projects/'+str( projectName ) )
		if( console.data['currentProject'] == str( projectName ) ):
			console.data['currentProject'] = ''
			console.replaceJson()

		for project in console.data['projects']:
			if( project['name'] == str( projectName ) ):
				console.data['projects'].remove( project )
				console.replaceJson()
				break

		print 'succesfully'







	def generateProject(self, projectName, console):
		print 'Checking if Node and npm are installed'
		try:
			console.runCommand('npm -v')
			print 'succesfully'

			print 'installing react native CLI'
			console.runCommand('npm install -g create-react-native-app')
			print 'succesfully'

			print 'creating project: '+str( projectName )
			console.runCommand( 'create-react-native-app projects/'+str( projectName ) )
			print 'succesfully'

			print 'adding your project into JSON conf file'
			newProject = {'name' : projectName , 'components': [], 'services': [], 'routes': [] }
			console.data['projects'].append( newProject )
			console.replaceJson()
			print 'succesfully'

			print 'Moving and checking directory work'
			os.chdir( 'projects/'+str( projectName ) )
			print os.getcwd()

			print 'Installing axios for fetching'
			console.runCommand('npm install axios --save')
			print 'succesfully'

			print 'Installing react-native-router-flux for routing system'
			console.runCommand('npm install react-native-router-flux --save')
			print 'succesfully'

			print 'Installing native-base for styling css'
			console.runCommand('npm install native-base --save')
			print 'succesfully'

			print 'Installing socket for events configuration (real time apps)'
			console.runCommand('npm install socket.io-client --save')
			print 'succesfully'

			print 'Doing some amazinGenerator magic...'
			console.runCommand('rm -rf App.test.js')
			console.runCommand('rm -rf App.js')
			console.runCommand('cp ../../share/App.template App.js')
			console.runCommand('mkdir src')
			os.chdir( 'src' )
			console.runCommand('mkdir Services')
			console.runCommand('mkdir Components')
			console.runCommand('mkdir Routes')
			console.runCommand('cp ../../../share/base.template Services/base.js')
			console.runCommand('cp ../../../share/routes.template Routes/index.js')
			console.runCommand('cp ../../../share/index.template index.js')
			os.chdir('../../../')
			print 'succesfully'
			print 'Now by using your project you can create components, services, etc.'

		except OSError:
			print "Error: You have not installed NPM, please install it before continue..."
			
		
