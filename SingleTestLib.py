#SingleTestLib - Universal RobotFramework test library for implementing Python based keywords
#See RobotFramework docs for help: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-libraries
__version__ = '0.1'

import os, sys, inspect
from datetime import datetime
import robot.api.logger as logger
try :
    from PIL import ImageGrab                    # For screen capture via Python Image Library (PIL)
except :
    ImageGrab = None

keywordsSubfolderPath = os.path.join(os.path.dirname(__file__), 'keywords')
sys.path.append(keywordsSubfolderPath)
from keywords import *
	
class SingleTestLib:
	#retrieves keywords from all modules, stored in the "keywords" subfolder
	#it requires the properly configured __init__.py file in this subfolder, which sets the "__all__" variable - it's necessary for the dynamic bulk module import
	def get_keyword_names(self):				
		keywords = []
		#iterate through all files in the folder .. no subfolders for now!
		for name in os.listdir(keywordsSubfolderPath):
			if name.endswith(".py") and not name.endswith("__init__.py"):
				module = name[:-3] #use file name as the base
				for member in inspect.getmembers(globals()[module], inspect.isfunction): #this returns all module attributes, including members and functions
					functionName = member[0]
					if not functionName.startswith('_'): #this filters out the internal module members
						keywords.append(module + "." + functionName) #make a name using the module name and the function name
		
		return keywords
	#---------------------------------------------------------------
	
	#calls the requested function with requested arguments
	def run_keyword(self, name, args, kwargs):		
		try:
			func = self._findFunction(name)		 
			result = func(*args, **kwargs)
			return result
		except Exception as ex:
			#log the function name
			#logger.error("Error in keyword '{0}'".format(name))
			#take a screenshot and log it
			if ImageGrab == None:	#no PIL imagegrab library available
				logger.warn("Failed taking screenshot - Python Imaging Library (PIL) is not installed")
			else:
				try:
					common.Screenshot("Screenshots\\{0} - {1}.png".format(name, datetime.now().strftime('%Y-%m-%d__%H_%M_%S')))
				except Exception as e:
					logger.warn("Failed taking screenshot: {0}".format(e))
			raise ex #reraise the exception
	#---------------------------------------------------------------
	
	#returns function documentation - basically what stays as a multiline comment directly after the function name
	def get_keyword_documentation(self, name):
		if name != '__intro__':
			func = self._findFunction(name)
			return inspect.getdoc(func)
		
	#---------------------------------------------------------------
	
	#returns function signature - which arguments it can take.
	#it allows RobotFramework to check the arguments accuracy in calling keywords even before trying to run the keyword itself.
	#also quite useful for RIDE intellisense function.
	def get_keyword_arguments(self, name):
		func = self._findFunction(name)
		fullArgSpec = inspect.getargspec(func)
		
		args = fullArgSpec[0]
		varargs = fullArgSpec[1]
		kwargs = fullArgSpec[2]
		defaults = fullArgSpec[3]
		
		#add to usual positional args possible defaults
		if defaults is not None:
			i = len(args) - 1
			for default in reversed(defaults):
				args[i] += "=" + str(default)
				i -= 1
		resultStr = args
		
		#named args if available
		if varargs is not None:
			resultStr.append("*" + varargs)
		#free argument assignment if available
		if kwargs is not None:
			resultStr.append("**" + kwargs)
			
		return resultStr
	#---------------------------------------------------------------
	
	#searches the requested function using reflection.
	#it looks inside the imported keyword modules using the following name separation "KeywordModule.Keyword"
	#returns the found function as an object
	def _findFunction(self, name):
		#separate module name from function name based on dot ('.')
		splitted = name.split('.')
		functionName = splitted[len(splitted)-1] #last part is always the function name
		moduleName = name[:-len("." + functionName)] #all in front of the function name is the module name		
		return getattr(globals()[moduleName], functionName)
	#---------------------------------------------------------------