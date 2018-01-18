*** Settings ***
Library           SingleTestLib.py

*** Test Cases ***
TestOne
    Example Module.Start    arg1    arg2
    Example Module.Close
