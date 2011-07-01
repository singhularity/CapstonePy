import Pyro4
from Pyro4 import  naming 
from optparse import OptionParser
import InstructionParser
import ConfigConstants

class GetetConfigs:
         
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
        nameserver=naming.locateNS(options.host, options.port)
        
        if len(args)==1:
            resultdict =  nameserver.list()
        else:
            resultdict = nameserver.list(prefix=args[1]), "- prefix '%s'" % args[1]
        list = []
        for name, uri in sorted(resultdict.items()):
            obj = Pyro4.Proxy(uri)
            if not isinstance(obj,Pyro4.naming.NameServer):
                list.append(obj)
        self.nodeList = list
        return list
    
    def getNumberofNodes(self):
        if self.nodeList != None:
            return self.nodeList.count()
        else:
            return self.getNodeList().count()
        
    def setNodeDetails(self):
        self.nodes = InstructionParser.getNodeDetails(ConfigConstants.__RESOURCE_DIR + "\\" + ConfigConstants.__CONFIG_FILE) 
    
    def getNumberOfConfigNodes(self):
            if self.nodes == None:
                numNodes, capacity  = self.setNodeDetails()                
            else:
                numNodes , capacity = self.nodes
            return numNodes
    
    def getRamCapacity(self):
        if self.nodes == None:
            numNodes, capacity = self.setNodeDetails()
        else:
            numNodes, capacity = self.nodes
        return capacity
    
        
    def getInstructionSet(self):
        return InstructionParser.getInstructionSet()
    
    def getServerRam(self):
        if self.serverSpecs == None:
            serverRam, maxData = self.serverSpecs
        else:
            serverRam, maxData = self.serverSpecs
        return serverRam
    
    def getMaxData(self):
        if self.serverSpecs == None:
            serverRam, maxData = self.setServerSpecs()
        else:
            serverRam, maxData = self.serverSpecs
        return maxData
    
    def setServerSpecs(self):
        self.serverSpecs = InstructionParser.getServerDetails(ConfigConstants.__RESOURCE_DIR + "\\" + ConfigConstants.__CONFIG_FILE)
        
    def writeConfig(self,configlist):
        try:
            configFile = open(ConfigConstants.__RESOURCE_DIR + "\\" + ConfigConstants.__CONFIG_FILE, 'w')
            for paramName, value in configlist:
                configFile.writeline(paramName + "\n" + value)
            configFile.close()
        except:
            print "Cannot write configurations to config file :: ", configFile 