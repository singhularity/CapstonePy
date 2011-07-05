import os
import InstructionParser

class InstructionParser:
    def __init__(self):   
        self.__NODES = "Nodes"
        self.__NODE_RAM_CAPACITY = "RamCap"
        self.__SERVER_RAM_CAPCITY = "ServerRam"
        self.__MAX_DATA = "MaxData"
        self.__GRAPH_HEAD_FILE = "graphHead.txt"
        self.__GRAPH_LINE_TAIL_FUNCTION = "lneFunctionTail.txt"
        self.__GRAPH_PIE_TAIL_FUNCTION = "lineFunctionTail.txt"
        self.__GRAPH_LINE_HEAD_FUNCTION = "lineFunctionHead.txt"
        self.__GRAPH_PIE_HEAD_FUNCTION = "pieFunctionHead.txt"
        self.__GRAPH_TAIL_FILE = "graphTail.txt" #file containing tail HTML
        self.__SIMULATION_CHARTS_HTML = "SimulationCharts" #name for simulation chart file
        self.__SERVER_CONTENT_FILE = "serverContent.txt" #file which holds server disk contents
        self.__OUTPUT_FILE_DIR = "simulations" #the simulations are generated in this directory
        self.__DATE_FORMAT = "yyyyMMDDss" #date format for simulation run folders
        self.__HOME_DIR = os.getcwd() #gets the current directory
        self.__RESOURCE_DIR = self.__HOME_DIR + r"\resources" #location for instruction files for clients
        self.__NODE_USAGE_MESSAGE = r"Usage :: java <AlgorithmClass> <host> <port> <RamAmount> <NodeName> <InstructionFile>"
        self.__SERVER_USAGE_MESSAGE = r"Usage :: java <AlgorithmClass> <host> <port> <RamAmount> <NodeName> <InstructionFile>"
        self.__SERVER_NAME = "Server"
        self.__CONFIG_FILE = "configFile.txt"
        self.__READ_INSTRUCTION = 0 #token for a "READ" from the server
        self.__DISK_CAPACITY = 5000 #Max disk capacity for server
        instructionparser = InstructionParser()
        self.__DELAY_STATS = instructionparser.getDelayStats(self.__RESOURCE_DIR + r"/" + self.__CONFIG_FILE)
        self.__DISK_DELAY = self.__DELAY_STATS.get(0)
        self.__CLIENT_DELAY = self.__DELAY_STATS.get(1)
        self.__MANAGER_DELAY = self.__DELAY_STATS.get(2)
        self.__LOCAL_CACHE_DELAY = self.__DELAY_STATS.get(3)
        self.__DEBUG_SWITCH =  True if self.__DELAY_STATS.get(4) == 0  else False  #turns logging On/Off
        self.__DELAY_SWITCH = True if self.__DELAY_STATS.get(5) == 0 else False #turns sleep On/Off
        self.__HOST = "localhost"
        self.__PORT = 9901
        #Configuration tokens
        self.__DISK_DELAY_TOKEN = "DiskDelay"
        self.__CLIENT_DELAY_TOKEN = "ClientDelay"
        self.__MANAGER_DELAY_TOKEN = "ManagerDelay"
        self.__LOCAL_CACHE_DELAY_TOKEN = "LocalCacheDelay"
        self.__LOG_MESSAGES_TOKEN = "LogMessages"
        self.__ADD_DELAY_TOKEN = "AddDelay"