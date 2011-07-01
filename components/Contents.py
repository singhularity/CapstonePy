import datetime

class Contents:
    def __init__(self,content):
        self.content = content
        self.accessDate = datetime.datetime.now() 
        self.frequency = 0
        
    def accessContent(self):
        self.frequency += 1
        self.accessDate = datetime.datetime.now()
        return self
    
    
    def __str__(self): 
        return self.content, " :: ", self.accessDate