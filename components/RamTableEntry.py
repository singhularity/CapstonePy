class RamTableEntry:
    def __init__(self, clientNode, content):
        self.clientNode = clientNode
        self.content = content
        
    def __repr__(self):
        return self.clientNode + " :: " + self.content
    
    def __cmp__(self, entry):
        return (self.content == entry.content) and (self.clientNode == entry.clientNode)
    
    def __ne__(self, entry):
        return not self.__cmp__(entry)       