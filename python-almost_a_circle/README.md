
Python Project README
Background Context
This project focuses on a comprehensive review of Python fundamentals, covering various topics such as import, exceptions, classes, inheritance, file handling, unit testing, and more. Additionally, it delves into advanced concepts like args and kwargs, serialization/deserialization, and JSON handling.

Step by Step Guide
Write the first class Base

Start by creating the base class.
Write the class Rectangle that inherits from Base

Create a Rectangle class inheriting from Base.
Update Rectangle class with validation and methods

Add validation to setter methods and instantiation.
Implement methods like area() and display().
Update Rectangle class with method overrides

Override methods such as __str__ and display() to enhance functionality.
Update Rectangle class with update() method

Implement the update() method to assign arguments to attributes.
Write the class Square that inherits from Rectangle

Create the Square class inheriting from Rectangle.
Update Square class with size methods

Add getter and setter methods for the size attribute.
Update Square class with update() method

Implement the update() method to assign attributes.
Update classes with dictionary methods

Add to_dictionary() methods to both Rectangle and Square classes.
Update Base class with file handling methods

Add class methods like savetofile(), fromjsonstring(), create(), and loadfromfile() for file handling and serialization.
Resources
args/kwargs
JSON encoder and decoder
unittest module
Python test cheatsheet
Learning Objectives
Upon completion of this project, you should be able to:

Understand and implement unit testing in a large project.
Serialize and deserialize Python classes.
Read and write JSON files effectively.
Utilize *args and **kwargs for flexible function arguments.
Handle named arguments in functions efficiently.
Requirements
Python Scripts
Editors: vi, vim, emacs
Interpretation/Compilation: Ubuntu 20.04 LTS using python3 (version 3.8.5)
File Endings: All files should end with a new line
Shebang: First line of all files should be #!/usr/bin/python3
README.md: Mandatory at the root of the project folder
Code Style: Pycodestyle (version 2.7.*)
Executability: All files must be executable
File Length: Tested using wc
Documentation: Modules, classes, and functions should be documented with descriptive sentences
Python Unit Tests
Editors: vi, vim, emacs
File Endings: All files should end with a new line
Test Folder: All test files should be inside a folder named tests
Module: Unittest module must be used
File Organization: Tests should follow the same structure as the project
Execution: Tests should be executed using python3 -m unittest discover tests
Collaboration
Collaboration on test cases is strongly encouraged to ensure thorough coverage of all edge cases and scenarios. Working together can help in identifying and addressing potential issues effectively.