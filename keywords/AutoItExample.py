#Prerequisites:
# 1) Install pywin32 - https://sourceforge.net/projects/pywin32/files/pywin32/
# 2) Install AutoIt with AutoItX COM-Control - https://www.autoitscript.com/site/autoit/downloads/

import win32com.client as _comClient

_autoIt = _comClient.Dispatch("AutoItX3.Control")
_winTitle = "[CLASS:Notepad; REGEXPTITLE:Untitled|Unbenannt.*]" #main identification data for the application window
_winHandle = ""

def Start(FilePath="notepad.exe"):
	"""
	Launches the application using the specified EXE file path.
	Waits for an appropriate window to appear.
	Sets the internal the window handle, which will be used later for accessing the proper window.
	
	_Parameters:_
		- *FilePath* - path to the application EXE file
	"""
	global _autoIt
	global _winTitle	
	global _winHandle
	
	print("Start command: {}".format(FilePath))
	_autoIt.Run(FilePath, "", _autoIt.SW_MAXIMIZE)
	assert _autoIt.WinWait(_winTitle, "", 10), "Error: Application start window not appeared"
	
	_winHandle = _autoIt.WinGetHandle(_winTitle)
	
def Close():
	"""
	Closes the previously opened application window.
	Uses either the internally set window handle or the default window title in case the handle is not set.
	Waits for the window to disappear.
	"""
	global _autoIt
	global _winTitle
	global _winHandle
	
	#it's better to use an exact handle to find a window
	#but if it's by chance empty, use the default title
	if _winHandle == "":			
		titleStr = _winTitle
	else:
		titleStr = "[HANDLE:{0}]".format(_winHandle)
	
	#Closes the window
	_autoIt.WinClose(titleStr)