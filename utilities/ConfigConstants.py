import os
import InstructionParser

__NODES = "Nodes"
__NODE_RAM_CAPACITY = "RamCap"
__SERVER_RAM_CAPCITY = "ServerRam"
__MAX_DATA = "MaxData"
__GRAPH_HEAD_FILE = "graphHead.txt"
__GRAPH_LINE_TAIL_FUNCTION = "lneFunctionTail.txt"
__GRAPH_PIE_TAIL_FUNCTION = "lineFunctionTail.txt"
__GRAPH_LINE_HEAD_FUNCTION = "lineFunctionHead.txt"
__GRAPH_PIE_HEAD_FUNCTION = "pieFunctionHead.txt"
__GRAPH_TAIL_FILE = "graphTail.txt" #file containing tail HTML
__SIMULATION_CHARTS_HTML = "SimulationCharts" #name for simulation chart file
__SERVER_CONTENT_FILE = "serverContent.txt" #file which holds server disk contents
__OUTPUT_FILE_DIR = "simulations" #the simulations are generated in this directory
__DATE_FORMAT = "yyyyMMDDss" #date format for simulation run folders
__HOME_DIR = os.getcwd() #gets the current directory
__RESOURCE_DIR = __HOME_DIR + r"\resources" #location for instruction files for clients
__NODE_USAGE_MESSAGE = r"Usage :: java <AlgorithmClass> <host> <port> <RamAmount> <NodeName> <InstructionFile>"
__SERVER_USAGE_MESSAGE = r"Usage :: java <AlgorithmClass> <host> <port> <RamAmount> <NodeName> <InstructionFile>"
__SERVER_NAME = "Server"
__CONFIG_FILE = "configFile.txt"
__READ_INSTRUCTION = 0 #token for a "READ" from the server
__DISK_CAPACITY = 5000 #Max disk capacity for server
__DELAY_STATS = InstructionParser.getDelayStats(__RESOURCE_DIR + r"/" + __CONFIG_FILE)
__DISK_DELAY = __DELAY_STATS.get(0)
__CLIENT_DELAY = __DELAY_STATS.get(1)
__MANAGER_DELAY = __DELAY_STATS.get(2)
__LOCAL_CACHE_DELAY = __DELAY_STATS.get(3)
__DEBUG_SWITCH =  True if __DELAY_STATS.get(4) == 0  else False  #turns logging On/Off
__DELAY_SWITCH = True if __DELAY_STATS.get(5) == 0 else False #turns sleep On/Off
__HOST = "localhost"
__PORT = 9901
#Configuration tokens
__DISK_DELAY_TOKEN = "DiskDelay"
__CLIENT_DELAY_TOKEN = "ClientDelay"
__MANAGER_DELAY_TOKEN = "ManagerDelay"
__LOCAL_CACHE_DELAY_TOKEN = "LocalCacheDelay"
__LOG_MESSAGES_TOKEN = "LogMessages"
__ADD_DELAY_TOKEN = "AddDelay"