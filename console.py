#!/usr/bin/python3
"""This is the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of File to exit the program"""
        print()
        return True

    def empty_line(self):
        """Empty line doesn't execute anything"""
        pass

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
