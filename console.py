#!/usr/bin/python3
"""This is the entry point of the command interpreter"""


import argparse
import cmd
from models.base_model import BaseModel
from models import storage
import re


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and print the id"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = storage.classes()
                new_instance.save()
                print(new_instance.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            all_objects = storage.all()
            if obj_key in all_objects:
                print(all_objects[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Dletes an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            all_objects = storage.all()
            if obj_key in all_objects:
                del all_objects[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of instamces
        based on class name or all"""
        args = arg.split()
        all_objects = storage.all()
        obj_list = []
        if not arg:
            for key, value in all_objects.items():
                obj_list.append(str(value))
            print(obj_list)
        elif args[0] not in storage.classes():
            print("** class doen't exist **")
        else:
            for key, value in all_objects.items():
                if key.split(".")[0] == args[0]:
                    obj_list.append(str(value))
            print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on class name and id
        by adding or updating an attribute
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            all_objects = storage.all()
            if obj_key in all_objects:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    setattr(all_objects[obj_key], args[2], args[3].strip('"'))
                    all_objects[obj_key].save()
            else:
                print("** no instance found **")

        def default(self, line):
            """Module for customized model commands"""
            line_list = line.split('.')
            if len(line_list) >= 2:
                model_name = line_list[0]
                command = line_list[1]

                if command == "all()":
                    self.do_all(model_name)
                elif command == "count()":
                    self.count(model_name)
                elif command.startswith("show"):
                    args = command.split()
                    if len(args) == 2:
                        self.do_show(f"{model_name} {args[1]}")
                    else:
                        print("Invalid show command")
                elif command.startswith("destroy"):
                    args = command.split()
                    if len(args) == 2:
                        self.do_destroy(f"{model_name} {args[1]}")
                    else:
                        print("Invalid destroy command")
                elif command.startswith("update"):
                    args = command.split()
                    if len(args) == 4:
                        key = f"{model_name} {args[1]}"
                        attribute = args[2]
                        value = args[3].strip('""')
                        self.do_update(f'{key} {attribute} "{value}"')
                    else:
                        print("Invalid update command")
                else:
                    cmd.Cmd.default(self, line)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
