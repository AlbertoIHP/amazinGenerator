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
			print '\033[92m'+'succesfully\n'

			print '\033[93m'+'installing react native CLI\n'
			console.runCommand('npm install -g create-react-native-app')
			print '\033[92m'+'succesfully'

			print '\033[93m'+'creating project: '+str( projectName )
			console.runCommand( 'create-react-native-app projects/'+str( projectName ) )
			print '\033[92m'+'succesfully\n'



			print '\033[93m'+'Moving and checking directory work\n'
			os.chdir( 'projects/'+str( projectName ) )
			print os.getcwd()
			print '\033[92m'+'succesfully\n'

			print '\033[93m'+'Doing some amazinGenerator magic... \n'




			console.runCommand('cp ../../share/kikiriwi.png '+str( projectName )+'.png')



			console.runCommand('rm -rf app.json')
			packageText = open( '../../share/app.json.template', 'r' ).read().replace('kukuriwi', str( projectName ) )
			open( 'app.json', 'w' ).write( packageText )




			
			console.runCommand('npm install --save axios')
			console.runCommand('npm install --save native-base')
			console.runCommand('npm install --save socket.io-client')
			console.runCommand('npm install --save moment')
			console.runCommand('npm install --save react-navigation')



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
			console.runCommand('cp -r ../../../share/mainComponent Components')
			os.chdir('../../../')


			print '\033[93m'+'adding your project into JSON conf file \n'
			newProject = { 
				'name' : projectName , 
				'components': [ { 'name': 'mainComponent', 'state': [ {'name': 'title', 	'value': 'mainComponent works' } ], 
					  'functions': [ 
						{'name': 'constructor', 'params': [ { 'name': 'props' } ], 'returnVal': False }, 
						{'name': 'closeDrawer', 'params': [ ], 'returnVal': False }, 
						{'name': 'openDrawer', 'params': [ ], 'returnVal': False }, 
						{'name': 'render', 'params': [ ], 'returnVal': True } ] }, 
					{'name': 'SideBar', 'state' : [ {'name': 'shadowOffsetWidth', 'value': 1}, {'name': 'shadowRadius', 'value': 4} ], 
					'functions': [ 
						{'name': 'constructor', 'params': [ { 'name': 'props' } ], 'returnVal': False }, 
						{'name': 'render', 'params': [ ], 'returnVal': True } ] } ], 
				'services': [], 
				'tabs' : [ { name: tab1 } ], 
				'routes': [] }
			console.data['projects'].append( newProject )
			console.replaceJson()
			print '\033[92m'+'succesfully\n'

			print '\033[94m'+'Now by using your project you can create components, services, etc.'

		except OSError:
			print '\033[91m'+"Error: You have not installed NPM, please install it before continue..."
			
		
