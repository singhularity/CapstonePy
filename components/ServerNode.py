import Node
class ServerNode(Node):
    def __init_(self, host, port, myRam, nodeName):
        super.__init__(host, port, myRam, nodeName, None)
    
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