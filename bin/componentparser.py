from subprocess import call
import json
import io
import os
from fuzzywuzzy import fuzz


class ComponentParser(object):


	def showComponents( self,currentProject,console ):
		if( currentProject == '' ):
			print '\033[91m'+"Error: You have to select one project to create a component"
		else:
			for project in console.data['projects']:
				if( project['name'] == currentProject ):
					#print project['components']
					for component in project['components']:
						print "- "+str( component['name'] )
						#print "- "+str( component['name'] )

						#console.data['currentProject'] = str( projectName )
						#console.replaceJson()
						#print "succesfully"
					break
				else:
					print "There are no project with name: "+str( projectName )



	def createComponent( self, currentProject, componentName, console ):
		# First we check if there is a selected project
		if( currentProject == '' ):
			print '\033[91m'+"Error: You have to select one project to create a component"
		else:
			print '\033[93m'+"Configurating your component for the project: "+currentProject

			# If user, has selected a project early, we will move into components folder
			os.chdir( 'projects/'+str( currentProject )+"/src/Components" )

			#We create a new folder in which one we will save the component files
			console.runCommand( 'mkdir '+str( componentName ) )

			# Then we move into the folder
			os.chdir( str( componentName ) )


			# We save in this vars, the names of our both files for any component
			componentFileName = "index.js"
			stylesFileName = 'styles.js'




			# We go and get the template file and read it
			styles = open( '../../../../../share/styles.template', 'r' ).read()

			# Then we write a file with the name that we set before( line 30 ) with the content extracted from the tempalte file
			open( stylesFileName, 'w' ).write( styles )


			# Now we initialize the content of our component
			componentText = ''

			# We open the component template
			with open('../../../../../share/Component.template') as f:

				# We walk throw each line of the file that we had read
			    for line in f:

			    	# We use fuzzy function to find our secret word and replace it by the standar of a component name
			    	result = self.fuzzy_replace( 'kukuriwi', componentName+'Component', line )

			    	# If there are no secret word, we just put the line as it is
			    	if( str(result) == 'None' ):
			    		componentText = componentText+line+'\n'

			    	# But if we find the secret word, we will replace it by the new one with kukuriwi changed
			    	else:
			    		componentText = componentText+str(result)+'\n'





			# Then we just open and write a new file with the content that we made
			open( componentFileName, 'w' ).write( componentText )


			# As component and styles are already created we now go to the routes file
			os.chdir( '../../Routes' )




			# First we get the template single route file, and read it, and replace our scret word by the component name
			singleRoute = open( '../../../../share/singleRoute.template', 'r' ).read().replace('kukuriwi', componentName+'Component' )





			# As well as we need the single route put inside the router, we also have to import that component
			# That is why we create this standar ES6 import of our component
			importText = 'import '+componentName+'Component'+' from "../Components/'+componentName+'"'












			# We create the single menu elemtn for the drawer (SideBar)
			singleDrawerElement =  open( '../../../../share/singleMenu.template', 'r' ).read().replace('kukuriwi', componentName+'Component' )









			# We initialize the file content that, our routes file will have
			routesText = ''
			singleDrawerMenuAdded = False
			leaveOneWithout = False

			# We open the one that were created when the projects was initialized
			with open( '../Components/mainComponent/SideBar/index.js' ) as f:

				# And we walk throw each line as we did before
			    for line in f:
			    	# If import is done, we check if signle rout was not added and there is exactly our kukuriwi word to replace it by single route inside the router tags
			    	if( len( str( line ) ) == 21 and singleDrawerMenuAdded == False ):
			    		routesText = routesText+'           '+singleDrawerElement.replace('//kukuriwi', singleDrawerElement )+',\n'+'          //kukuriwi'+'\n'
			    		singleDrawerMenuAdded = True

			    	# Else we check if the content has something (not a clean one) and we add the line
			    	elif(len( str(line) ) == 1  and leaveOneWithout == False):
			    		routesText = routesText+str(line)+'\n'
			    		leaveOneWithout = True
			    	elif( len( str( line ) ) > 1 ):
			    		routesText = routesText+str(line)


			console.runCommand('rm -rf ../Components/mainComponent/SideBar/index.js')


			# And we create a new one with the same standart name
			open( '../Components/mainComponent/SideBar/index.js', 'w' ).write( routesText )


			# We create this flags to now when we already add the import, the route and leave one clean line to
			# Import future components
			importAdded = False
			routeAdded = False
			leaveOneWithout = False




			# We initialize the file content that, our routes file will have
			routesText = ''

			# We open the one that were created when the projects was initialized
			with open( 'index.js' ) as f:

				# And we walk throw each line as we did before
			    for line in f:

			    	# We check if there is an clean line and if the import was not added to add it
			    	if( len( str( line ) ) == 1 and importAdded == False ):
			    		routesText = routesText+importText+'\n'
			    		importAdded = True


			    	# If import is done, we check if signle rout was not added and there is exactly our kukuriwi word to replace it by single route inside the router tags
			    	elif( len( str( line ) ) == 21 and routeAdded == False ):
			    		routesText = routesText+'           '+singleRoute.replace('//kukuriwi', singleRoute )+',\n'+'          //kukuriwi'+'\n'
			    		routeAdded = True

			    	# If import and single route are done, we check if we can leave one clean line (Just one)
			    	elif( len( str(line) ) == 1 and leaveOneWithout == False):
			    		routesText = routesText+str(line)+'\n'
			    		leaveOneWithout = True

			    	# Else we check if the content has something (not a clean one) and we add the line
			    	elif( len( str( line ) ) > 1 ):
			    		routesText = routesText+str(line)




			# Finally we just delete the old version of the file
			os.remove('index.js')

			# And we create a new one with the same standart name
			open( 'index.js', 'w' ).write( routesText )

			# Then we just come back to our main amazinGenerator directory
			os.chdir( '../../../..' )





			print '\033[93m'+'adding your component into JSON conf file \n'
			newComponent = 	{
					'name': componentName,
					'state': [ {'name': 'title', 	'value': componentName+' works' } ],
					'functions': [
						{
							'name': 'constructor',
							'params': [ { 'name': 'props' } ],
							'returnVal': False
						},
						{
							'name': 'render',
							'params': [ ],
							'returnVal': True
						},
						]
				}

			for project in console.data['projects']:
				if( project['name'] == console.data['currentProject'] ):
					project['components'].append( newComponent )
					break

			console.replaceJson()
			print '\033[92m'+'succesfully\n'




	def fuzzy_replace( self, str_a, str_b, orig_str ):
		# Length to read orig_str chunk by chunk
	    l = len(str_a.split())
	    splitted = orig_str.split()
	    for i in range(len(splitted)-l+1):
	        test = " ".join(splitted[i:i+l])
	        #Using fuzzwuzzy library to test ratio
	        if fuzz.ratio(str_a, test) > 75:
	            before = " ".join(splitted[:i])
	            after = " ".join(splitted[i+1:])
	            #Output will be sandwich of these three strings
	            return before+" "+str_b+" "+after
