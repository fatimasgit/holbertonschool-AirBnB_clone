import cmd

"""
This file is for command line with Python
"""

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
    
    def do_hello(self, arg):
        """Print a greeting message"""
        print("Hello! Welcome to MyCmd.")
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()