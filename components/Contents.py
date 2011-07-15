import datetime
import types

class Contents(object):
    def __init__(self,content):
        self.content = content
        self.accessdate = datetime.datetime.now() 
        self.frequency = 0
        
    def accessContent(self):
        self.frequency += 1
        self.accessdate = datetime.datetime.now()
        return self   
    
    def __repr__(self): 
        return self.content, " :: ", self.accessdate
    
    def __eq__(self, compcont):
        if type(compcont) == types.ListType:       
            return self.content == compcont[0]
        elif isinstance(compcont, Contents):
            return self.content == compcont.content
        else:
            return self.content == compcont
    
    def __ne__(self, compcont):        
        return not self.__eq__(compcont)