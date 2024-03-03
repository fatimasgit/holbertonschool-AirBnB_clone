import json

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
            self.objects[key] = obj
    
    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        
        data = json.dump(self.__objects)
        
        with open(self.__file_path, "w") as file:
            file.write(data)
    
    def reload(self):


        try:
            # Open file for read
            with open(self.__file_path, "r") as file:
                data = file.read()
            
            self.__objects = json.loads(data)
        except FileNotFoundError:
            # Handle the case where the file doesn't exist
            self.__objects = {}