from subprocess import call
import json
import io
import os


class TabParser(object):
	def createTab( self, currentProject, componentName, console ):
		print "Se debe crear tab"