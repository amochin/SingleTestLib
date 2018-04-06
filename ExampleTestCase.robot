*** Settings ***
Library           SingleTestLib.py

*** Test Cases ***
TestOne
    Example Module.Start    arg1    arg2
    Example Module.Close
    Auto It Example.Start
    Sleep    2 seconds
    Auto It Example.Close
    Selenium Example.Open Home Page
    Sleep    2 seconds
    Selenium Example.Close
    Sikuli Example.Start
    Sleep    2 seconds
    Sikuli Example.Close
