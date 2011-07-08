from components import Node
from components import RamSimulator
from components import RamTableEntry
import sys

class ClientNode(Node.Node):
    def __init__(self, host, port, myRam, nodeName, instructionFile):
        Node.Node.__init__(self, host, port, myRam, nodeName, instructionFile)
       
    def pushContent(self,content, configurator):
        insertedFlag = super(ClientNode,self).getMyRam().pushContent(content)        
        if insertedFlag:
            self.broadcastEvent("Push Content",RamTableEntry.RamTableEntry(self, content))
        else:                        
            removed = super(ClientNode,self).getMyRam().LRU()
            super(ClientNode,self).getMyRam().pushContent(content)
            self.broadcastEvent("Push removed Content",RamTableEntry.RamTableEntry(self, removed))

def main(args):
    ram = RamSimulator.RamSimulator(int(args[3]))
    ClientNode(args[1], int(args[2]), ram, args[4], args[5])

if __name__ == "__main__":
    main(sys.argv)    
                
        
    