class QueryFacet:
    def __init__(self,key = 0,value=0):
      self.key=key
      self.value=value

   

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value=value
       




q=QueryFacet()
q.key=100
q.value="rajitha"
print(q.key)
print(q.value)