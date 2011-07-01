class ServerMonitor:
    def __init__(self):
        self.entries = {}
    
    def addEntry(self,content, clientNode):
        if content not in self.entries:
            self.entries[content] = clientNode
    
    def getContent(self, clientNode, content):
        if content in self.entries:
            return self.entries[content]
        else:
            self.addEntry(content, clientNode)
    
    def removeContent(self, content, clientNode):
        if self.entries[content] != clientNode:
            self.entries[content] = clientNode
    
        
            