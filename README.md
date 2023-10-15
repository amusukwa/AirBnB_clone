##AirBnB PROJECT

## Welcome to the AirBnB clone project!

## First step: Writing a command interpreter to manage our AirBnB objects.

## The AirBnB clone. This project will be linked with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

* First, a parent class (called BaseModel) is put in place to take care of the initialization, serialization and deserialization of your future instances
* A simple flow of serialization/deserialization is created: Instance <-> Dictionary <-> JSON string <-> file
* All classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel are created
* The first abstracted storage engine of the project: File storage is created
* All unittests to validate all our classes and storage engine are also created

A command interpreter, also known as a command-line interpreter or command-line interface (CLI), is a text-based interface that allows users to interact with a computer or software by entering textual commands. It is a means of providing instructions to a computer system by typing commands and receiving responses in text form.

In a command interpreter, users typically enter commands as text strings, and the interpreter processes these commands to perform various tasks or operations. Command interpreters are commonly used for tasks like managing files and directories, configuring system settings, executing programs, and interacting with the operating system and software applications.

## Execution
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

* But also in non-interactive mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
