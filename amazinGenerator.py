from bin.commandline import CommandLine
import re
import os
if __name__ == '__main__':
	console = CommandLine()

	while( True ):
		option = raw_input(' amazinGenerator ('+console.data['currentProject']+') >> ')
		command = option.split(' amazinGenerator ('+console.data['currentProject']+') >> ')
		if( command[0] == 'exit'):
			break
		elif( command[0] == 'run project'):
			if( console.data['currentProject'] == ''):
				print "You have to use one project to run it"
			else:
				os.chdir('projects/'+str( console.data['currentProject'] ) )
				console.runCommand('npm start')			
		elif( len( command ) == 1 and re.search( '[a-zA-Z]', command[0] ) ):
			console.execute( command[0] )
		else:
			print "We could not recognize your command "
			console.displayHelp()