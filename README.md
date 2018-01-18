# SingleTestLib
Universal RobotFramework test library for implementing Python based keywords

# Introduction
RobotFramework is an incredible test automation framework with great features for writing keyword-driven tests and reporting.
It has a lot of test libraries, e.g. _SeleniumLibrary_ or _AutoItLibrary_.

However using low-level keywords from these libraries directly in RF test cases is often not really comfortable (think about loops, some logical, arithmetic and string operations etc.).

A solution is **moving the mid-level keywords to test libraries** and implementing them with the whole power of a programming language (e.g. Python or Java).
There are different tools and approaches for that. Basically you can either create your own test libraries or take one of already existing solutions - and _SingleTestLib_ is one of them.

Unlike other tools, _SingleTestLib_ doesn't help you to create multiple RF test libraries - instead, it acts as a **single entry point to all your keywords** (though allowing to structure them).

With _SingleTestLib_ you implement keywords just as usual Python functions, ordering them in the module structure.
The _SingleTestLib_ scans all functions in .py modules in the _keywords_ subfolder and makes them available as keywords in RF test cases.

# Key points
- Implement complex keywords in Python
- No need to reference every module as separate test library in RF test cases and maintain the list - you just reference the _SingleTestLib_ only once
- Keywords are available in RF via _module name_._function name_ names - easy search and use
- Enjoy all benefits of RIDE intelligent functions - autocomplete, getting arguments and docs
- Automatic taking screenshots in case of failed keyword execution

# Quick Start 
- Reference the _SingleTestLib.py_ file as a test library in your .robot test cases
- Create .py modules in the _keywords_ subfolder and implement functions inside modules
- That's it! Functions are immediately available from the .robot test cases via combined names _module name_._function name_

See module and test case examples.

# Requirements
- Python (so far tested with Python 2.7)
- RobotFramework - http://robotframework.org/
- Pillow library for taking screenshot - https://pillow.readthedocs.io/en/5.0.0/
