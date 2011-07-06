import os
     
NODES = "Nodes"
NODE_RAM_CAPACITY = "RamCap"
SERVER_RAM_CAPCITY = "ServerRam"
MAX_DATA = "MaxData"
GRAPH_HEAD_FILE = "graphHead.txt"
GRAPH_LINE_TAIL_FUNCTION = "lneFunctionTail.txt"
GRAPH_PIE_TAIL_FUNCTION = "lineFunctionTail.txt"
GRAPH_LINE_HEAD_FUNCTION = "lineFunctionHead.txt"
GRAPH_PIE_HEAD_FUNCTION = "pieFunctionHead.txt"
GRAPH_TAIL_FILE = "graphTail.txt" #file containing tail HTML
SIMULATION_CHARTS_HTML = "SimulationCharts" #name for simulation chart file
SERVER_CONTENT_FILE = "serverContent.txt" #file which holds server disk contents
OUTPUT_FILE_DIR = "simulations" #the simulations are generated in this directory
DATE_FORMAT = "yyyyMMDDss" #date format for simulation run folders 
HOME_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) #gets the current directory                
RESOURCE_DIR = HOME_DIR + r"\resources" #location for instruction files for clients
NODE_USAGE_MESSAGE = r"Usage :: java <AlgorithmClass> <host> <port> <RamAmount> <NodeName> <InstructionFile>"
SERVER_USAGE_MESSAGE = r"Usage :: java <AlgorithmClass> <host> <port> <RamAmount> <NodeName> <InstructionFile>"
SERVER_NAME = "Server"
CONFIG_FILE = "configFile.txt"
READ_INSTRUCTION = 0 #token for a "READ" from the server
DISK_CAPACITY = 5000 #Max disk capacity for server
HOST = "localhost"
PORT = 9901
#Configuration tokens
DISK_DELAY_TOKEN = "DiskDelay"
CLIENT_DELAY_TOKEN = "ClientDelay"
MANAGER_DELAY_TOKEN = "ManagerDelay"
LOCAL_CACHE_DELAY_TOKEN = "LocalCacheDelay"
LOG_MESSAGES_TOKEN = "LogMessages"
ADD_DELAY_TOKEN = "AddDelay"
DELAY_STATS = []
DISK_DELAY = None
CLIENT_DELAY = None
MANAGER_DELAY = None
LOCAL_CACHE_DELAY = None
DEBUG_SWITCH =  None  #turns logging On/Off
DELAY_SWITCH = None #turns sleep On/Off

def getStats(stats):    
    for i in stats:       
        DELAY_STATS.append(i)    
    setStats()

def setStats():
    
    DISK_DELAY = DELAY_STATS[0]
    CLIENT_DELAY = DELAY_STATS[1]
    MANAGER_DELAY = DELAY_STATS[2]
    LOCAL_CACHE_DELAY = DELAY_STATS[3]
    DEBUG_SWITCH =  True if DELAY_STATS[4] == 0  else False  #turns logging On/Off
    DELAY_SWITCH = True if DELAY_STATS[5] == 0 else False #turns sleep On/Off
