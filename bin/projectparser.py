from subprocess import call
import json
import io
import os


class ProjectParser(object):



	def showProjects( self, console ):
		for project in console.data['projects']:
			print "- "+str( project['name'] )



	def useProject( self, projectName, console ):
		for project in console.data['projects']:
			if( project['name'] == projectName ):
				console.data['currentProject'] = str( projectName )
				console.replaceJson()
				print "succesfully"
				break
			else:
				print "There are no project with name: "+str( projectName )






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



			print 'Moving and checking directory work'
			os.chdir( 'projects/'+str( projectName ) )
			print os.getcwd()


			print 'Doing some amazinGenerator magic...'



			print "Cleaning your NPM cache, this may take a several minutes..."
			console.runCommand('npm cache clean --force')


			console.runCommand('rm -rf package.json')
			console.runCommand('rm -rf node_modules')
			console.runCommand('rm -rf package-lock.json')
			console.runCommand('cp ../../share/kikiriwi.png kikiriwi.png')




			packageText = open( '../../share/package.template', 'r' ).read().replace('kukuriwi', str( projectName ) )
			open( 'package.json', 'w' ).write( packageText )
			console.runCommand('ls -la')
			console.runCommand('rm -rf app.json')
			packageText = open( '../../share/app.json.template', 'r' ).read().replace('kukuriwi', str( projectName ) )
			open( 'app.json', 'w' ).write( packageText )




			
			console.runCommand('npm install')



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


			print 'adding your project into JSON conf file'
			newProject = {'name' : projectName , 'components': [], 'services': [], 'routes': [] }
			console.data['projects'].append( newProject )
			console.replaceJson()
			print 'succesfully'

			print 'succesfully'
			print 'Now by using your project you can create components, services, etc.'

		except OSError:
			print "Error: You have not installed NPM, please install it before continue..."
			
		
