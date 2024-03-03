#!/usr/bin/python3
"""
This file is for command line with Python
"""

import cmd
from models.base_model import BaseModel

# Classes
classes = {
    "BaseModel": BaseModel,
    # "Amenity": Amenity,
    # "City": City,
    # "Place": Place,
    # "Review": Review,
    # "State": State,
    # "User": User
    }

class HBNBCommand(cmd.Cmd):
    """
    Command line class with Python
    """
    
    def default(self, line):
        """Handle unrecognized commands"""
        if line == "help":
            self.do_help("")  # Call custom help function
        else:
            print("Unrecognized command:", line)
    
    def get_prompt(self):
        """ (hbnb) - prompt """
        return "(hbnb)"
    
    def emptyline(self):
        """Called when an empty line is entered"""
        pass  # Do nothing when an empty line is entered
    
    def cmdloop(self, intro=None):
        """ Set initial prompt """
        self.prompt = self.get_prompt()
        return super().cmdloop(intro)
    
    def do_custom_help(self):
        """ Help function """
        print("AirBnB clone - The console")
    
    def do_quit(self, arg):
        """ Function for quit """
        return True
    
    def do_EOF(self, arg):
        """ Function for quit """
        return True

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()