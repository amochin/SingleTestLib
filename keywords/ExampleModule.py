#Handle for this particular SUT Example App window
_winHandle = "" #Name of this variable starts with underscore (_), so it's not available from outside

#This function is available as keyword from RobotFramework
def Start(FilePath, SomeParameter):
	"""
	Opens the SUT Example App with the specified parameter.
	Waits for an appropriate window to appear.
	Sets the internal the window handle, which will be used later for accessing the proper SUT Example App window.
	
	_Parameters:_
		- *FilePath* - path to the SUT Example App EXE file
		- *SomeParameter* - Some parameter        
    
    Tags: tag1, tag2
	"""
	global _winHandle
	
	#Call the application file with the parameter	
	pass
	
	#SUT-specific wait
	pass
	
	#Set some global vars, e.g. handle
	_winHandle = _getHandle()
	
#Another keyword for RF
#Notice that the file itself is a module (not class) and the functions are not class methods.
#So no need to transfer the 'self' argument.
def Close():
	"""
	Closes SUT
	"""
	pass

#Name of this functions starts with underscore (_), so it's not available as keyword from RobotFramework
def _getHandle():
	#magic
	pass