import Instruction
import GetSetConfigs
from components import Contents
from ConfigConstants import *

def readServerContents(self,serverContentFile):
    serverContent = []
    try:
        contentReader = open(serverContentFile,'r')
        serverContent.append(contentReader.read().split())
    except:
        print "Cannot open server content file :: ", serverContentFile 
    finally:
        contentReader.close()    
    return serverContent

def getInstructionSet(self):
    getConfigs = GetSetConfigs()
    nodeList = getConfigs.getNodeList()
    instructionSet = []
    for node in nodeList:
        instructionSet.append(node)
        
def getInstructionFromFile(file):
    try:
        nodeFile = open(file, 'r')
        instructions = []        
        for inslist in (nodeFile.readline().replace('\n','').split(" ")):
            instructions.append(Instruction(inslist[0], inslist[1], Contents(inslist[2])))
        return instructions
    except:
        print "Cannot open instruction file :: " , file
    finally:
        file.close()
        
def getNodeDetails(file):
    try:
        nodeContent = open(file.replace('\\','/'), 'r')
        line = nodeContent.readline().replace('\n', '')
        while line:        
            if line == NODES:
                numNodes = int(nodeContent.readline().replace('\n', ''))
            elif line == NODE_RAM_CAPACITY:          
                ramCapacity = int(nodeContent.readline().replace('\n', ''))
            else:
                line = nodeContent.readline().replace('\n', '')
            line = nodeContent.readline().replace('\n', '')
        nodeContent.close()        
        return numNodes, ramCapacity
    except Exception as expt:
        print expt
        print "Cannot open config file :: ", file
        
def getServerDetails(file):
    try:        
        instructionReader =open(file,'r')
        line = instructionReader.readline().replace('\n','')
        while line:
            if line == SERVER_RAM_CAPCITY:
                serverRamCapacity = int(instructionReader.readline().replace('\n',''))
            elif line == MAX_DATA:
                maxData = int(instructionReader.readline().replace('\n',''))
            else:
                line = instructionReader.readline().replace('\n','')
            line = instructionReader.readline().replace('\n','')
        instructionReader.close()        
        return serverRamCapacity, maxData
    except Exception as expt:
        print expt
        print "Cannot open config file :: ", file
        
def getDelayStats(file):
    statFile = open(file.replace('\\','/'), 'r')
    delayList = []       
    try:        
        line = statFile.readline().replace('\n', '')
        while line:        
            if line == DISK_DELAY_TOKEN:                            
                delayList.append(int(statFile.readline().replace('\n', '')))            
            elif line == CLIENT_DELAY_TOKEN:
                delayList.append(int(statFile.readline().replace('\n', '')))
            elif line == MANAGER_DELAY_TOKEN:
                delayList.append(int(statFile.readline().replace('\n', '')))
            elif line == LOCAL_CACHE_DELAY_TOKEN:
                delayList.append(int(statFile.readline().replace('\n', '')))
            elif line == LOG_MESSAGES_TOKEN:
                delayList.append(int(statFile.readline().replace('\n', '')))
            elif line == ADD_DELAY_TOKEN:
                delayList.append(int(statFile.readline().replace('\n', '')))
            else:
                line = statFile.readline().replace('\n', '')
            line = statFile.readline().replace('\n', '')
        print delayList
        getStats(delayList)
        statFile.close()
    except Exception as excpt:
        print excpt        
        print "Cannot open configfile :: ", file 