#Prerequisites:
# 1) Install pywin32 - https://sourceforge.net/projects/pywin32/files/pywin32/
# 2) Install AutoIt with AutoItX COM-Control - https://www.autoitscript.com/site/autoit/downloads/

import win32com.client as _comClient

_autoIt = _comClient.Dispatch("AutoItX3.Control")
_winTitle = "Untitled" #main identification data for the application window

def Start(FilePath="notepad.exe"):
	"""
	Launches the application using the specified EXE file path.
	Waits for an appropriate window to appear.	
	
	_Parameters:_
		- *FilePath* - path to the application EXE file
	"""
	global _autoIt
	global _winTitle	
	
	print("Start command: {}".format(FilePath))
	_autoIt.Run(FilePath, "", _autoIt.SW_MAXIMIZE)
	assert _autoIt.WinWait(_winTitle, "", 10), "Error: Application start window not appeared"