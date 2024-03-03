import json
from json.decoder import JSONDecodeError

class FileStorage:
    """
    The class for storing data  
    """
    __file_path = "./file.json"
    __objects = {}
    
    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects
    
    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            if key == "password":
                json_objects[key].decode()
            json_objects[key] = self.__objects[key].to_dict(save_fs=1)
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)
    def reload(self):


        try:
            # Open file for read
            with open(self.__file_path, "r") as file:
                data = file.read()
            
            self.__objects = json.loads(data)
            
        except (FileNotFoundError, JSONDecodeError):
            # Handle the case where the file doesn't exist or is empty
            self.__objects = {}