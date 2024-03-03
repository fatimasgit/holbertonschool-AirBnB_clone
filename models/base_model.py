import uuid  #unik ID generate etmek ucun modul
from datetime import datetime  # datetime ucun modul

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())  #id generate edir
        self.created_at = datetime.now()  #id nin yaranma tarixi
        self.updated_at = datetime.now()  #id nin update olunma tarixi
        
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()
        #datetime update edir indikine uygun
        
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__  #class dictionary e add olunur
        obj_dict['created_at'] = self.created_at.isoformat()  #tarixi cevirir iso formata yeni regemli tarix formatina
        obj_dict['updated_at'] = self.updated_at.isoformat()  #eyni seyi update ucun de edi
        return obj_dict