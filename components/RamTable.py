class RamTable:
    def __init__(self, allContent, newContentList):
        self.allContent = {}
        self.nodeContentList = ()
    
    def addRamTableEntry(self,entry):
        self.addContent(entry.getContent())
        self.nodeContentList.__add__(entry)
    
    def addContent(self,content):
        if content in self.allContent:
            self.allContent[content] = (self.allContent[content] + 1)
        else:
            self.allContent[content] = 1
            
    def getNodeWithContent(self, content):
        for entry in self.nodeContentList:
            if entry.getContent() == content:
                return entry.getClientNode()
            
    def removeRamTableEntry(self,entry):
        self.removeContent(entry.getContent())
        del self.nodeContentList[entry]
    
    def removeContent(self,content):
        if content in self.allContent:
            newval = self.allContent.get(content)
            if ((newval - 1) == 0):
                self.alContent.remove(content)
            else:
                self.allContent[content] = (newval - 1)
                
    def getContentCopyCount(self, content):
        return -1 if content in self.allContent else self.allContent[content]
    
    def getMaxCountContent(self):
        maxCont = None
        maxCount = 0
        for content in self.allContent.keys():
            if maxCont is None or (self.allContent[content] > maxCount):
                maxCont = content
                maxCount = self.allContent[content]
        return maxCont        
    
    def getNodeForContent(self, content):
        for entry in self.nodeContentList:
            if entry.getContent() ==  content:
                return entry.getClientNode()
    
    def seeRamTable(self):
        print self.nodeContentList  
            
    
        
        
            
        
            
        
        