#!/usr/bin/python3
"""
This file is for command line with Python
"""

import cmd
from models.base_model import BaseModel
from models import engine
import shlex

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

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict 
    
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
        
    def do_show(self, arg):
        """ Prints the string representation of an instance based on the class name and id """
        args = arg.split()
        
        if (len(args) == 0):
            print("** class name missing **")
            return False
        
        if (args[0] in classes):
            if (len(args) > 1):
                key = args[0] + "." + args[1]
                if key in engine.storage.all():
                    print(engine.storage.all()[key])
                else:
                    print("** no instance found **")
            else: print("** instance id missing **")
        else: print("** class doesn't exist **")
    
    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if (len(args) == 0):
            print("** class name missing **")
        elif (args[0] in classes):
            if (len(args) > 1):
                key = args[0] + "." + args[1]
                if (key in engine.storage.all()):
                    engine.storage.all().pop(key)
                    engine.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if (len(args) == 0):
            obj_dict = engine.storage.all()
        elif (args[0] in classes):
            obj_dict = engine.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if (len(args) == 0):
            print("** class name missing **")
        elif (args[0] in classes):
            if (len(args) > 1):
                k = args[0] + "." + args[1]
                if (k in engine.storage.all()):
                    if (len(args) > 2):
                        if (len(args) > 3):
                            if (args[0] == "Place"):
                                if (args[2] in integers):
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif (args[2] in floats):
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(engine.storage.all()[k], args[2], args[3])
                            engine.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
            
if (__name__ == '__main__'):
    HBNBCommand().cmdloop()