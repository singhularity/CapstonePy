class RamTableEntry:
    def __init__(self, clientNode, content):
        self.clientNode = clientNode
        self.content = content
        
    def __str__(self):
        return self.clientNode + " :: " + self.content       