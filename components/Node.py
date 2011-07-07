from Observable import Observable
from utilities import InstructionParser
import Pyro4
import RamTableEntry

class Node(Observable, object):
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
        try:
            Pyro4.config.DOTTEDNAMES = "true"
            daemon = Pyro4.Daemon()
            ns=Pyro4.locateNS()
            uri = daemon.register(self)
            ns.register(nodeName, uri)
            daemon.requestLoop()
            print "available"
        except:
            print "Cannot bing node to naming Service.", nodeName
            
    def pushContent(self, content):
        if self.myRam.pushContent(content):
            self.broadcastEvent("PushContent", self,RamTableEntry(self, content))
        else:
            self.myRam.LRU()
            self.myRam.pushContent(content)
        return True
    
    def getContent(self, content):
        if self.myRam.getContent(content):
            self.broadcastEvent("GetContent", RamTableEntry(self, content))
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
        
    def __str__(self):
        return self.nodeName + " :: Client :: "
        
    
        