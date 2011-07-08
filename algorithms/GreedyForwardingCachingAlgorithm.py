from components import NetworkConfigurator
from components import ServerNode
from utilities import GetSetConfigs
import ClientNode
class GreedyForwardingCachingAlgorithm:
    def __init__(self,nodeRam, serverNode):
        self.nodeRam = nodeRam        
        self.serverNode = serverNode
        self.serverNode.getStr()
        self.nodeList = []
        self.configurator = NetworkConfigurator.NetworkConfigurator(self.nodeList)
        self.createNodes()        
    
    def createNodes(self):
        for newNode in GetSetConfigs.GetSetConfigs().getNodeList():
            self.configurator.observe(newNode)
            self.nodeList.append(newNode);
    
    def addContent(self, nodeNum, content):        
        for contents in content:
            if isinstance(self.nodeList[nodeNum], ServerNode.ServerNode):
                self.nodeList[nodeNum].pushContent(contents)
            else:
                receivednode = self.nodeList[nodeNum]                    
                receivednode.pushContent(contents,self.configurator)
                
    def readContent(self, clientNodeNum, content):
        clientNode = self.nodeList[clientNodeNum]           
        contentNode = self.getNeighbor(content)
        
        if  clientNode.getContent(content):
            clientNode.incrementLocalCacheHitCount()
            print "Local cache hit"
        elif contentNode != None:
            clientNode.incrementeighbourCacheHitCount()
            print "Content " + content + "fetched from peer " + contentNode + " :: " + clientNode             
        elif self.serverNode.getContent(content):
            clientNode.incrementDiskAccessCount()
            self.addContent(clientNodeNum, content)            
        else:
            print "Not found!"
        
    def getNeighbor(self,content):
        return self.configurator.getNodeWithContent(content)
    
    def getServerNode(self):
        return self.serverNode
    
    def getNodeList(self):
        return self.nodeList