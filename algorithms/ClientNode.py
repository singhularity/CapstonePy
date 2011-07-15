from components import Node
from components import RamSimulator
from components import RamTableEntry
import sys
import Pyro4

class ClientNode(Node.Node):
    """Client Nodes"""
    def __init__(self, host, port, myRam, nodeName, instructionFile):
        Node.Node.__init__(self, host, port, myRam, nodeName, instructionFile)
               
    def pushContent(self,content, configurator):        
        insertedFlag = Node.Node.pushContent(self,content)        
        if insertedFlag:
            self.broadcastEvent("Push Content",RamTableEntry.RamTableEntry(self, content))
        else:                        
            removed = Node.Node.getMyRam(self).LRU()
            Node.Node.pushContent(content)
            self.broadcastEvent("Push removed Content",RamTableEntry.RamTableEntry(self, removed))            

def main(args):
    ram = RamSimulator.RamSimulator(int(args[3]))
    client = ClientNode(args[1], int(args[2]), ram, args[4], args[5])    
    try:
        #if(self.nodeName != "Server"):
        Pyro4.config.DOTTEDNAMES = "true"
        daemon = Pyro4.Daemon()
        ns=Pyro4.locateNS()
        uri = daemon.register(client)
        ns.register(client.nodeName, uri)
        daemon.requestLoop()
        print "available"            
    except:
        print "Cannot bing node to naming Service.", client.nodeName

if __name__ == "__main__":
    main(sys.argv)    
                
        
    