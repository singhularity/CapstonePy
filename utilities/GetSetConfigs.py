import Pyro4
from Pyro4 import  naming 
from optparse import OptionParser
#from components import ServerNode
import InstructionParser
from ConfigConstants import *
import re

class GetSetConfigs(object):
    def __init__(self):
        self.capacity = None
        self.numNodes = None
        self.serverRam = None
        self.maxData = None
        self.nodeList = []         
    def getNodeList(self):
        args = ["list"]
        usage = "usage: %prog [options] command [arguments]\nCommand is one of: " \
                    "register remove removematching list listmatching ping"
        parser = OptionParser(usage=usage)
        
        parser.add_option("-n", "--host", dest="host", help="hostname of the NS")
        parser.add_option("-p", "--port", dest="port", type="int",
                              help="port of the NS (or bc-port if host isn't specified)")
        parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="verbose output")
        options, args = parser.parse_args(args)
        Pyro4.config.DOTTEDNAMES = "true"
        nameserver=naming.locateNS(options.host, options.port)
        
        if len(args)==1:
            resultdict =  nameserver.list()
        else:
            resultdict = nameserver.list(prefix=args[1]), "- prefix '%s'" % args[1]
        
        for name, uri in sorted(resultdict.items()):
            Pyro4.config.DOTTEDNAMES = "true"            
            obj = Pyro4.core.Proxy(uri)
            obj.__pyroAttributes = True            
            #if not isinstance(obj,Pyro4.naming.NameServer):# and not isinstance(obj,ServerNode.ServerNode):
            if re.search('\ANode',name):# and not isinstance(obj,ServerNode.ServerNode):
                print name                
                self.nodeList.append(obj)                  
        return self.nodeList
    
    def getNumberofNodes(self):
        if self.nodeList != None:
            return self.nodeList.__len__()
        else:
            return self.getNodeList().__len__()
        
    def setNodeDetails(self):
        instructionParser = InstructionParser        
        self.numNodes, self.capacity = instructionParser.getNodeDetails(RESOURCE_DIR + "\\" + CONFIG_FILE)
       
    def getNumberOfConfigNodes(self):
        if self.numNodes == None:
            self.setNodeDetails()    
        return self.numNodes
    
    def getRamCapacity(self):
        if self.capacity == None:
            self.setNodeDetails()        
        return self.capacity
    
        
    def getInstructionSet(self):
        return InstructionParser.getInstructionSet(self)
    
    def getServerRam(self):
        if self.serverRam == None:
            self.setServerSpecs()
        return self.serverRam
    
    def getMaxData(self):
        if self.maxData == None:
            self.setServerSpecs()        
        return self.maxData
    
    def setServerSpecs(self):        
        self.serverRam, self.maxData = InstructionParser.getServerDetails(RESOURCE_DIR + "\\" + CONFIG_FILE)
        
    def writeConfig(self,configlist):
        try:            
            configFile = open(RESOURCE_DIR + "\\" + CONFIG_FILE, 'w')
            for paramName, value in configlist:
                configFile.writeline(paramName + "\n" + value)
            configFile.close()
        except:
            print "Cannot write configurations to config file :: ", configFile 