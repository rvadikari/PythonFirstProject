from abc import ABC,abstractmethod
from Iresult import IResult
class IQueryParser(ABC):
    @abstractmethod
    def parse():
        pass


class CriteriaJson(IQueryParser):
    def __init__(self,name):
        self._name=name
        
    def parse(self)->IResult.result:
        try:
            print(self._name)
        except:
            return "exception occured"
    
        

c1=CriteriaJson("rajitha")
c1.parse()