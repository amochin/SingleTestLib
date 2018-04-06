#This module might contain automation keywords for a web app or or part of it
#selenium and webdriver for your browser must be installed first - see https://pypi.python.org/pypi/selenium
from selenium import webdriver

_homePageUrl = "http://google.com"
_browser = None

#This function is available as keyword from RobotFramework
def OpenHomePage():
	"""
	Opens the home page and checks the title
	"""
	global _homePageUrl
	global _browser
	
	#choose your browser
	
	#InternetExplorer usage - Enable Protected Mode in IE must be set to the same value (enabled or disabled) for all zones.
	#_browser =  webdriver.Ie()
	
	#Chrome usage
	_browser = webdriver.Chrome()	
	_browser.get(_homePageUrl)
	assert "Google" in _browser.title

#This function is available as keyword from RobotFramework
def Close():
	"""
	Closes the current browser session
	"""
	global _browser	
	_browser.quit()