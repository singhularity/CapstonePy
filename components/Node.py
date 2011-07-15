from Observable import Observable
from utilities import InstructionParser
import RamTableEntry

class Node(Observable, object):
    """Nodes"""
    def __init__(self, host, port, myRam, nodeName, instructionFile):
        Observable.__init__(self)
        self.myRam = myRam
        self.nodeName = nodeName
        self.diskAccessCount = 0
        self.localCacheHitCount = 0
        self.neighbourCacheHitCount = 0
        self.diskAccessCount = 0
        self.localCacheHitCount = 0
        self.instructionSheet = []
        
        if instructionFile:
            self.instructionSheet = InstructionParser.getInstructionFromFile(instructionFile)
    
    def getMyRam(self):        
        return self.myRam
            
    def pushContent(self, content):               
        if self.myRam.pushContent(content):
            self.broadcastEvent("PushContent", self,RamTableEntry.RamTableEntry(self, content))
        else:            
            self.myRam.LRU()
            self.myRam.pushContent(content)
        return True      
    
    def getContent(self, content):                
        if self.myRam.getContent(content):            
            self.broadcastEvent("GetContent", RamTableEntry.RamTableEntry(self, content))
            return True
        return False           
    
    def incrementDiskAccessCount(self):
        self.diskAccessCount += 1
        
    def incrementLocalCacheHitCount(self):
        self.localCacheHitCount += 1
        
    def incrementNeighbourCacheHitCount(self):
        self.neighbourCacheHitCount += 1
    
    def getInstructionSheet(self):
        return InstructionParser.getInstructionFromFile(r"C:\GITProjects\CapstonePy\resources\node1.txt")
    
    def getNodeName(self):
        return self.nodeName
        
    def __repr__(self):
        return self.nodeName + " :: Client :: "
    
    def __eq__(self, node):
        return self.nodeName == node.nodeName
    
    def __ne__(self, node):
        return not self.__eq__(node) 
    
    
        
    
        