from Observable import Observer
import ServerNode
import Node
import RamTable
import RamTableEntry
import random
class NetworkConfigurator(Observer):
    def __init__(self, nodeList):
        self.nodeList = nodeList
        for node in nodeList:
            if isinstance(node, ServerNode):
                self.serverNode = node
        self.globalTable = RamTable.RamTable()
        
    def getNodeWithContent(self,content):
        #TODO Add Delay
        return self.globalTable.getNodeWithContent(content)
    
    def processEvent(self,notifierObject,eventName,*args):             
        if isinstance(notifierObject, Node.Node):                        
            self.globalTable.addRamTableEntry(args[0])
    
    def removeGlobalContent(self, removeEntry):
        self.globalTable.removeRamTableEntry(removeEntry)
    
    def isSinglet(self, content):
        return self.globalTable.getContentCopyCount(content) == 1
    
    def getRamdomNode(self):
        self.nodeList[random.randint(self.nodeList.count() + 1)]
        
    def getRichChunkNode(self):
        maxContent = self.globalTable.getMaxCountContent()
        return self.globalTable.getNodeForContent(maxContent), maxContent