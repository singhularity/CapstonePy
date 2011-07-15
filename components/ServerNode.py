import Node
import utilities.GetSetConfigs
from utilities.ConfigConstants import *
from utilities import InstructionParser
import Pyro4

import components.RamSimulator
class ServerNode(Node.Node,object):
    def __init__(self, host, port, myRam, nodeName):
        self.diskCapacity = None
        self.contents = []                
        self.diskCapacity = DISK_CAPACITY
        self.diskAccess = 0
        self.cacheAccess = 0
        self.contents = InstructionParser.readServerContents(RESOURCE_DIR.replace('\\','/') + "/" + SERVER_CONTENT_FILE)
        Node.Node.__init__(self,host, port, myRam, nodeName, None)            
   
    def getContent(self, content):
        #TODO Add Delay
        if not super(ServerNode,self).getContent(content):
            #Add Delay
            if content in self.contents:
                print "Content " + str(content.content) + " fetched from the disk!"
                super(ServerNode,self).pushContent(content)
                self.diskAccess += 1                
        else:
            print "Content " + str(content.content) + " fetched from server cache!"
            self.cacheAccess += 1
            
            
        return True
    
    def __repr__(self):
        return super(ServerNode,self).getNodeName() + " :: Server "   
    
def main(args):
    configs = utilities.GetSetConfigs.GetSetConfigs()
    ramCapacity = configs.getServerRam()    
    server = ServerNode(args[0], args[1], components.RamSimulator.RamSimulator((ramCapacity)), SERVER_NAME)
    try:
        #if(self.nodeName != "Server"):
        Pyro4.config.DOTTEDNAMES = "true"
        daemon = Pyro4.Daemon()
        ns=Pyro4.locateNS()
        uri = daemon.register(server)
        ns.register(server.nodeName, uri)
        daemon.requestLoop()
        print "available"            
    except:
        print "Cannot bing node to naming Service.", server.nodeName  
    
if __name__ == "__main__":
    main(["localhost", "9090"])    
    