import json
from json.decoder import JSONDecodeError
from models.base_model import BaseModel
from models.user import User

classes = {
    # "Amenity": Amenity,
    "BaseModel": BaseModel,
    # "City": City,
    # "Place": Place,
    # "Review": Review,
    # "State": State,
    "User": User
}

class FileStorage:
    """
    The class for storing data  
    """
    __file_path = "file.json"
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
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass