from components import Node
from components import RamSimulator
from components import RamTableEntry

class ClientNode(Node.Node):
    def __init__(self, host, port, myRam, nodeName, instructionFile):
        Node.Node(host, port, myRam, nodeName, instructionFile)
       
    def poshContent(self,content, configurator):
        if super.getMyRam().pushContent(content):
            self.broadcastEvent("Push Content",self, content)
        else:
            removed = super.getMyRam().LRU()
            super.getMyRam().pushContent(content)
            self.broadcastEvent(RamTableEntry.RamTableEntry(self, content))

def main(args):
    ram = RamSimulator.RamSimulator(int(args[2]))
    ClientNode(args[0], int(args[1]), ram, args[3], args[4])

if __name__ == "__main__":
    main(['localhost', '9090', '10','Node1',r"C:\GITProjects\CapstonePy\resources\node1.txt"])    
                
        
    