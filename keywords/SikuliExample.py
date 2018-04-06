#Prerequisites:
# 1) Install SikuliX - http://sikulix.com/
# 2) Install RobotFramework SikuliLibrary - https://github.com/rainmanwy/robotframework-SikuliLibrary

import os, xmlrpclib, subprocess
from robot.libraries.BuiltIn import BuiltIn

def _sikuli():
	"""
	Imports and returns current instance of the SikuliLibrary via RobotFramework
	"""
	imageDir=os.path.join(os.path.dirname(__file__), 'SikuliImages')	
	
	BuiltIn().import_library("SikuliLibrary")
	_sikuli = BuiltIn().get_library_instance('SikuliLibrary')
	_sikuli.run_keyword('addImagePath', [imageDir])
	return _sikuli

def Start():
	"""
	Launches the application and waits for the window to appear
	"""
	print("click Windows Start button")
	_sikuli().run_keyword('click', ['windows_start_menu.png'])
	print("input application name")
	_sikuli().run_keyword('inputText', ['', 'Internet Explorer'])
	print("click application icon")
	_sikuli().run_keyword('click', ['ie.png'])
	print("wait for application to appear")		
	_sikuli().run_keyword('waitUntilScreenContain', ['ie_navigation_buttons.png', '5'])	
	
def Close():
	"""
	Closes the application and waits for the window to disappear
	"""
	print("close the application")
	_sikuli().run_keyword('doubleClick', ['ie_navigation_buttons.png', 0, 0])
	print("wait for the window to close")
	_sikuli().run_keyword('waitUntilScreenNotContain', ['ie_navigation_buttons.png', '5'])