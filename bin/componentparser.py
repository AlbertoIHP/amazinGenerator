from subprocess import call
import json
import io
import os
from fuzzywuzzy import fuzz


class ComponentParser(object):


	def createComponent( self, currentProject, componentName, console ):
		if( currentProject == '' ):
			print "Error: You have to select one project to create a component"
		else:
			print "Configurating your component for the project: "+currentProject
			os.chdir( 'projects/'+str( currentProject )+"/src/Components" )
			console.runCommand( 'mkdir '+str( componentName ) )
			os.chdir( str( componentName ) )

			componentFileName = "index.js"
			stylesFileName = 'styles.js'



			#Creation of styles file
			styles = open( '../../../../../share/styles.template', 'r' )
			open( stylesFileName, 'w' ).write( styles.read() )

			componentText = ''

			#Reading the template to replace for the name component
			with open('../../../../../share/Component.template') as f:
			    for line in f:
			    	result = self.fuzzy_replace( 'kukuriwi', componentName+'Component', line )
			    	if( str(result) == 'None' ):
			    		componentText = componentText+line+'\n'
			    	else:
			    		componentText = componentText+str(result)+'\n'



			
			open( componentFileName, 'w' ).write( componentText )

			os.chdir( '../../Routes' )


			#Single route text
			singleRoute = open( '../../../../share/singleRoute.template', 'r' )
			singleRoute = singleRoute.read()
			singleRoute = singleRoute.replace('kukuriwi', componentName+'Component' )
			#Import text
			importText = 'import '+componentName+'Component'+' from "../Components/'+componentName+'"'





			importAdded = False
			routeAdded = False
			routesText = ''


			#Editing current Routes file
			with open( 'index.js' ) as f:
			    for line in f:
			    	if( len( str( line ) ) == 1 and importAdded == False ):
			    		routesText = routesText+importText+'\n'
			    		importAdded = True
			    	elif( len( str( line ) ) == 20 and routeAdded == False ):
			    		routesText = routesText+'           '+singleRoute.replace('//kukuriwi', singleRoute )+'\n'+'        	//kukuriwi'+'\n'
			    		routeAdded = True
			    	else:
			    		routesText = routesText+str(line)+'\n'



			os.remove('index.js')
			open( 'index.js', 'w' ).write( routesText )
			print "successfully"



	def fuzzy_replace( self, str_a, str_b, orig_str ):
	    l = len(str_a.split()) # Length to read orig_str chunk by chunk
	    splitted = orig_str.split()
	    for i in range(len(splitted)-l+1):
	        test = " ".join(splitted[i:i+l])
	        if fuzz.ratio(str_a, test) > 75: #Using fuzzwuzzy library to test ratio
	            before = " ".join(splitted[:i])
	            after = " ".join(splitted[i+1:])
	            return before+" "+str_b+" "+after #Output will be sandwich of these three strings




		