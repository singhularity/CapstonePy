import Node
import utilities.GetSetConfigs
from utilities.ConfigConstants import *
from utilities import InstructionParser

import components.RamSimulator
class ServerNode(Node.Node,object):
    def __init__(self, host, port, myRam, nodeName):
        self.diskCapacity = None
        self.contents = None                
        self.diskCapacity = DISK_CAPACITY
        self.contents = InstructionParser.readServerContents(RESOURCE_DIR.replace('\\','/') + "/" + SERVER_CONTENT_FILE)
        Node.Node.__init__(self,host, port, myRam, nodeName, None)            
   
    def getContent(self, content):
        #TODO Add Delay
        if not super(ServerNode,self).getContent(content):
            #Add Delay
            if content in self.contents:
                print "Content " + str(content.content) + " fetched from the disk!"
                super(ServerNode,self).getMyRam().pushContent(content)
                self.diskAccess += 1                
        else:
            print "Content " + str(content.content) + " fetched from server cache!"
            self.cacheAccess += 1
            
            
        return True
    
    def __str__(self):
        return super(ServerNode,self).getNodeName() + " :: Server "   
    
def main(args):
    configs = utilities.GetSetConfigs.GetSetConfigs()
    ramCapacity = configs.getServerRam()    
    ServerNode(args[0], args[1], components.RamSimulator.RamSimulator((ramCapacity)), SERVER_NAME)  
    
if __name__ == "__main__":
    main(["localhost", "9090"])    
    