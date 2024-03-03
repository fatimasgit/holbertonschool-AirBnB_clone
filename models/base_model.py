import uuid  #unik ID generate etmek ucun modul
from datetime import datetime  # datetime ucun modul
# Import the variable storage
from models import engine
# Import models
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        if (kwargs):
            # kwargs daxilinde key ve value ayirir
            for key, value in kwargs.items():
                # classda error verdi ona görə
                if (key != "__class__"):
                    # atribut elave edir, atribut - key
                    setattr(self, key, value) 
                
            # eger object yarananda id daxil edilmeyibse
            if (kwargs.get("id", None) is None): 
                self.id = str(uuid.uuid4())
            
            # Eger object yarananda created_at variable'a deger verilmeyibse
            if (kwargs.get("created_at", None) and type(self.created_at) is str):
                self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.now()
            
            if(kwargs.get("updateed_data",None) and type(self.updated_at) is str):
                self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.now()
                
        else:
            self.id = str(uuid.uuid4())  #id generate edir
            self.created_at = datetime.now()  #id nin yaranma tarixi
            self.updated_at = datetime.now()  #id nin update olunma tarixi
        
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()
        # If it’s a new instance (not from a dictionary representation), add a call to the method new(self) on storage
        engine.storage.new(self)
        # Save data
        engine.storage.save()
        
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__  #class dictionary e add olunur
        obj_dict['created_at'] = self.created_at.isoformat()  #tarixi cevirir iso formata yeni regemli tarix formatina
        obj_dict['updated_at'] = self.updated_at.isoformat()  #eyni seyi update ucun de edi
        return obj_dict