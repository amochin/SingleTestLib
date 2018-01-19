#This module might be a web app or or part of it
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
	_browser = webdriver.Chrome()
	_browser.get(_homePageUrl)
	assert "Google" in _browser.title

#This too
def Close():
	"""
	Closes the current browser session
	"""
	global _browser	
	_browser.quit()