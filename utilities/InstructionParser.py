import Instruction
import GetSetConfigs
from components import Contents
import ConfigConstants
import os

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
        for inslist in (nodeFile.readline().split(" ")):
            instructions.append(Instruction(inslist[0], inslist[1], Contents(inslist[2])))
        return instructions
    except:
        print "Cannot open instruction file :: " , file
    finally:
        file.close()
        
def getNodeDetails(file):
    try:
        nodeContent = open(file, 'r')
        configConstants = ConfigConstants()
        if nodeContent.readline() == configConstants.__NODES:
            numNodes = int(nodeContent.readline())
            if nodeContent.readline() == configConstants.__NODE_RAM_CAPACITY:          
                ramCapacity = int(nodeContent.readine())
        return numNodes, ramCapacity
    except:
        print "Cannot open config file :: ", file
        
def getServerDetails(file):
    try:
        configConstants = ConfigConstants()
        instructionReader =open(file,'r')
        if instructionReader.readline() == configConstants.__SERVER_RAM_CAPCITY:
            serverRamCapacity = int(instructionReader.readline())
            if instructionReader.readline() == configConstants.__MAX_DATA:
                maxData = instructionReader.readline()
        return serverRamCapacity, maxData
    except:
        print "Cannot open config file :: ", file
        
def getDelayStats(file):
    statFile = open(file.replace('\\','\\\\'), 'r')
    delayList = []       
    try:
        configConstants = ConfigConstants.ConfigConstants()       
        if statFile.readline() == configConstants.__DISK_DELAY_TOKEN:                        
            delayList.apend(int(statFile.readline()))            
        if statFile.readline() == configConstants.__CLIENT_DELAY_TOKEN:
            delayList.append(int(statFile.readline()))
        if statFile.readline() == configConstants.__MANAGER_DELAY_TOKEN:
            delayList.append(int(statFile.readline()))
        if statFile.readline() == configConstants.__LOCAL_CACHE_DELAY_TOKEN:
            delayList.append(int(statFile.readLine()))
        if statFile.readline() == configConstants.__LOG_MESSAGES_TOKEN:
            delayList.append(int(statFile.readline()))
        if statFile.readline() == configConstants.__ADD_DELAY_TOKEN:
            delayList.append(int(statFile.readline()))
        return delayList
    except Exception as excpt:
        print excpt
        print file.replace('\\','\\\\')
        print "Cannot open configfile :: ", file      
                
        
    
        