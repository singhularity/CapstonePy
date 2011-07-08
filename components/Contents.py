import datetime

class Contents(object):
    def __init__(self,content):
        self.content = content
        self.accessdate = datetime.datetime.now() 
        self.frequency = 0
        
    def accessContent(self):
        self.frequency += 1
        self.accessdate = datetime.datetime.now()
        return self   
    
    def __str__(self): 
        return self.content, " :: ", self.accessdate