from components import NetworkConfigurator
from components import ServerNode
from utilities import GetSetConfigs
import ClientNode
class GreedyForwardingCachingAlgorithm:
    def __init__(self,nodeRam, serverNode):
        self.nodeRam = nodeRam        
        self.serverNode = serverNode        
        self.nodeList = []
        self.configurator = NetworkConfigurator.NetworkConfigurator(self.nodeList)
        self.createNodes()        
    
    def createNodes(self):
        for newNode in GetSetConfigs.GetSetConfigs().getNodeList():
            self.configurator.observe(newNode)
            self.nodeList.append(newNode);                   
    
    def addContent(self, nodeNum, content):        
        #for contents in content:
        #try:
        if isinstance(self.nodeList[nodeNum], ServerNode.ServerNode):
            self.nodeList[nodeNum].pushContent(content)
        else:            
            receivednode = self.nodeList[nodeNum]                                                    
            receivednode.pushContent(content,self.configurator)
        #except:
            #print "Error :: " + str(receivednode.getNodeName())
                
    def readContent(self, clientNodeNum, content):
        clientNode = self.nodeList[clientNodeNum]           
        contentNode = self.getNeighbor(content)
        
        if  clientNode.getContent(content):
            print "Local cache hit"
            clientNode.incrementLocalCacheHitCount()            
        elif contentNode != None:
            print "Content " + str(content.content) + "fetched from peer " #+ contentNode + " :: " + clientNode 
            clientNode.incrementeighbourCacheHitCount()                        
        elif self.serverNode.getContent(content):
            print "fetched content :: " + content.content            
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