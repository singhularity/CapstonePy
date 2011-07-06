from ConfigConstants import *
from utilities import GetSetConfigs
from random import randint

class InstructionSetGenerator:
    def generateNodeInstructionSetFiles(self):              
        configs = GetSetConfigs.GetSetConfigs()
        self.numberOfNodes = configs.getNumberOfConfigNodes()
        self.maxDataRange = configs.getMaxData()
        self.minDataRange = 1
        
        self.__generateServerContents()
        
        try:            
            for i in range (0, self.numberOfNodes):
                writer = open(RESOURCE_DIR.replace('\\', '/') + "/" + "node" + str(i + 1) + ".txt", "w")
                instructions = self.__getRandomInstructions(i + 1)
                for instr in instructions:
                    writer.write(instr)
                writer.close()
        except Exception as expt:
            print expt
            print "Cannot open file for writing :: " +  RESOURCE_DIR.replace('\\', '/') + "/" + "node" + str(i + 1) + ".txt"
            
    def __getRandomInstructions(self, nodeNum):
        dataSize = self.maxDataRange * 0.2
        data = []
        dataBiased = []
        
        for i in range(0, int(dataSize)):
            data.append(randint(1,(self.maxDataRange - self.minDataRange + 1)))
        
        for j in range(0, int(dataSize)):
            dataBiased.append("0 " + str(nodeNum) + " " + str(data[randint(1,int(dataSize * 0.5))]) + "\n")
        return dataBiased
    
    def __generateServerContents(self):
        try:            
            diskContents = open(RESOURCE_DIR.replace('\\', '/') + "/" + SERVER_CONTENT_FILE, "w")
            for i in range(0, int(self.maxDataRange)):
                diskContents.write(str(i) + "\n")
            diskContents.close()
        except Exception as expt:
            print expt
            print "Cannot open servercontent file for writing :: ", RESOURCE_DIR.replace('\\', '/') + "/" + SERVER_CONTENT_FILE
        
def main():
    instructionSetGenerator = InstructionSetGenerator()
    instructionSetGenerator.generateNodeInstructionSetFiles()
        
if __name__ == "__main__":
    main()        
