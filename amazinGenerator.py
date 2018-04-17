from bin.commandline import CommandLine
import re

if __name__ == '__main__':
	console = CommandLine()

	while( True ):
		option = raw_input(' amazinGenerator >> ')
		command = option.split(' amazinGenerator >> ')
		if( command[0] == 'exit'):
			break
		elif( len( command ) == 1 and re.search( '[a-zA-Z]', command[0] ) ):
			console.execute( command[0] )

		else:
			print "We could not recognize your command "
			console.displayHelp()