class RamSimulator:
    def __init__(self, maxCapacity):
        self.maxCapacity = maxCapacity
        self.currentCapacity = maxCapacity
        self.ramContents = []

    def pushContent(self, content):        
        if not content in self.ramContents and (self.currentCapacity - 1) >= 0:            
            self.ramContents.append(content)
            self.currentCapacity -= 1
            return True
        #else:
            #print "Lru :: here " + str(content.content)
            #self.LRU()
            #self.pushContent(content)
            #return True           
        
    
    def LRU(self):
        mincont = None
        for cont in self.ramContents:
            if mincont is None or (mincont.accessdate > cont.accessdate):
                mincont = cont 
        if mincont != None:       
            self.ramContents.remove(mincont)
            self.currentCapacity -= 1        
            return mincont
    
    def removeContent(self, content):
        if content in self.ramContents:
            self.ramContents.remove(content)
            self.currentCapacity -= 1
    
    def getContent(self, content):
        if content in self.ramContents:
            content.accessContent()
            return True
        return False
    
    def getMinContent(self):
        mincont = None
        for cont in self.ramContents:
            if mincont is None or (mincont.accessdate > cont.accessdate):
                mincont = cont;
        return mincont
    
    def __repr__(self):
        return "MaxCapacity : " + self.maxCapacity + "; CurrentCapacity : " + self.currentCapacity
        
            