class RamSimulator:
    def __init__(self, maxCapacity):
        self.maxCapacity = maxCapacity
        self.currentCapacity = maxCapacity
        self.ramContents = []

    def pushContent(self, content):
        if not self.ramContents.__contains__(content) and (self.currentCapacity - 1) >= 0:
            self.ramContents.append(content)
            self.currentCapacity -= 1
            return True
        else:
            self.LRU()
            self.pushContent(content)           
        return False
    
    def LRU(self):
        mincont = None
        for cont in self.ramContents:
            if mincont is None or (mincont.accessDate > cont.accessdate):
                    mincont = cont        
        self.ramContents.remove(mincont)
        self.currentCapacity -= 1        
        return mincont
    
    def removeContent(self, content):
        if self.ramContents__contains(content):
            self.removeContent(content)
            self.currentCapacity -= 1
    
    def getContent(self, content):
        if self.ramContents__contains(content):
            content.accessContent()
            return True
        return False
    
    def getMinContent(self):
        mincont = None
        for cont in self.ramContents:
            if mincont is None or (mincont.accessDate > cont.accessDate):
                mincont = cont;
        return mincont
    
    def __str__(self):
        return "MaxCapacity : " + self.maxCapacity + "; CurrentCapacity : " + self.currentCapacity
        
            