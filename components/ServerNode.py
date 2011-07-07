import Node
import utilities.GetSetConfigs
from utilities.ConfigConstants import *

import components.RamSimulator
class ServerNode(Node.Node,object):
    def __init__(self, host, port, myRam, nodeName):
        Node.Node(host, port, myRam, nodeName, None)
    
    def setDiskCapacity(self, diskCapacity):
        self.diskCapacity = diskCapacity
        
    def addContent(self, contents):
        self.contents = contents
    
    def getContent(self, content):
        #TODO Add Delay
        if not super.getContent(content):
            #Add Delay
            if content in self.diskContent:
                super.getMyRam().pushContent(content)
                self.diskAccess += 1
                print "Content " + content + " fetched from the disk!"
        else:
            self.cacheAccess += 1
            print "Content " + content + " fetched from server cache!"
            
        return True
    
    def __str__(self):
        return super.getNodeName() + " :: Server "
    
def main(args):
    configs = utilities.GetSetConfigs.GetSetConfigs()
    ramCapacity = configs.getServerRam()    
    ServerNode(args[0], args[1], components.RamSimulator.RamSimulator((ramCapacity)), SERVER_NAME)
    
if __name__ == "__main__":
    main(["localhost", "9090"])    
    