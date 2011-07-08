from utilities import GetSetConfigs
import Pyro4
from utilities.ConfigConstants import *
from Pyro4 import  naming
from optparse import OptionParser
from utilities import InstructionParser
import Executor

class Launcher:
    def setParams(self, host, port):
        configs = GetSetConfigs.GetSetConfigs()
        self.instructionSet = configs.getInstructionSet()
        self.nodeRamCapacity = configs.getRamCapacity()
        self.numberOfNodes = configs.getNumberofNodes()
        self.server = None
        Pyro4.config.DOTTEDNAMES = "true"        
        self.server = Pyro4.core.Proxy("PYRONAME:Server")
        self.server.__pyroAttributes = True
        #print self.server
        #from components import ServerNode
        #self.server.__class__ = ServerNode.ServerNode
        #self.server.setDiskCapacity(DISK_CAPACITY)
        #self.server.addContent(InstructionParser.readServerContents(RESOURCE_DIR.replace('\\','/') + "/" + SERVER_CONTENT_FILE))        
        
    def launch(self, algorithm, className):
        for i in range(self.instructionSet.__len__()):
            launcher1 = Executor.Executor(self.numberOfNodes, algorithm)            
            launcher1.setInstructionSet(self.instructionSet[i])
            launcher1.start()