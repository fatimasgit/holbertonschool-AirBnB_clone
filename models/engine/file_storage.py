import json
from json.decoder import JSONDecodeError

"""
Storage file for storing the data
"""

class FileStorage:
    """
    The class for storing data  
    """
    __file_path = "./file.json"
    __objects = {}
    
    def all(self):
        """ Returns the dictionary __objects """
    
        return self.__objects
    
    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
    
    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)
    
    def reload(self):


        try:
            # Open file for read
            with open(self.__file_path, "r") as file:
                data = file.read()
            
            self.__objects = json.loads(data)
            
        except (FileNotFoundError, JSONDecodeError):
            # Handle the case where the file doesn't exist or is empty
            self.__objects = {}