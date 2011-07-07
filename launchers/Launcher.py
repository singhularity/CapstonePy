from utilities import GetSetConfigs
import Pyro4
from utilities.ConfigConstants import *
from Pyro4 import  naming
from optparse import OptionParser
from utilities import InstructionParser
import Executor
from components import ServerNode
class Launcher:
    def setParams(self, host, port):
        configs = GetSetConfigs.GetSetConfigs()
        self.instructionSet = configs.getInstructionSet()
        self.nodeRamCapacity = configs.getRamCapacity()
        self.numberOfNodes = configs.getNumberofNodes()
        self.server = None
        
        args = ["list"]
        usage = "usage: %prog [options] command [arguments]\nCommand is one of: " \
                    "register remove removematching list listmatching ping"
        parser = OptionParser(usage=usage)
        
        parser.add_option("-n", "--host", dest="host", help="hostname of the NS")
        parser.add_option("-p", "--port", dest="port", type="int",
                              help="port of the NS (or bc-port if host isn't specified)")
        parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="verbose output")
        options, args = parser.parse_args(args)
        nameserver=naming.locateNS(options.host, options.port)
        
        if len(args)==1:
            resultdict =  nameserver.list()
        else:
            resultdict = nameserver.list(prefix=args[1]), "- prefix '%s'" % args[1]
        
        for name, uri in sorted(resultdict.items()):
            obj = Pyro4.Proxy(uri)
            if isinstance(obj,ServerNode.ServerNode):# and not isinstance(obj,ServerNode.ServerNode):
                self.server = obj         
        
        self.server.setDiskCapacity(DISK_CAPACITY)
        self.server.addContent(InstructionParser.readServerContents(RESOURCE_DIR.replace('\\','/') + "/" + SERVER_CONTENT_FILE))
        
    def launch(self, algorithm, className):
        for i in range(self.instructionSet.__len()):
            launcher1 = Executor(self.numberOfNodes, algorithm)
            launcher1.setInstructionSet(self.instructionSet[i])
            launcher1.start()