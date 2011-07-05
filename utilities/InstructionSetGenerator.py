import ConfigConstants
from utilities import GetSetConfigs
import random

class InstructionSetGenerator:
    def generateNodeInstructionSetFiles(self):
        print "helo"
        inst = GetSetConfigs.GetSetConfigs
        configs = GetSetConfigs.GetSetConfigs
        self.numberOfNodes = configs.getNumberOfConfigNodes(configs)
        self.maxDataRange = GetSetConfigs().getMaxData()
        self.minDataRange = 1
        
        self.__generateServerContents()
        
        try:
            configConstants = ConfigConstants()
            for i in range (0, self.numberOfNodes):
                writer = open(configConstants.__RESOURCE_DIR + "\\" + "node" + (i + 1) + ".txt", "w")
                instructions = self.__getRandomInstructions(i + 1)
                for instr in instructions:
                    writer.write(instr)
                writer.close()
        except:
            print "Cannot open file for writing :: ", configConstants.__RESOURCE_DIR + "\\" + "node" + (i + 1) + ".txt"
            
    def __getRandomInstructions(self, nodeNum):
        dataSize = self.maxDataRange * 0.2
        data = []
        dataBiased = []
        
        for i in range(0, dataSize):
            data.append(random.randint(self.maxDataRange - self.minDataRange + 1))
        
        for j in range(0, dataSize):
            dataBiased.append("0 " + nodeNum + " " + data[random.randint(int(dataSize * 0.5)) + "\n"] )
        return dataBiased
    
    def __generateServerContents(self):
        try:
            configConstants = ConfigConstants()
            diskContents = open(configConstants.__RESOURCE_DIR + "\\" + configConstants.__SERVER_CONTENT_FILE, "r")
            for i in range(0, self.maxDataRange):
                diskContents.write(i + "\n")
            diskContents.close()
        except:
            print "Cannot open servercontent file for writing :: ", configConstants.__RESOURCE_DIR + "\\" + configConstants.__SERVER_CONTENT_FIL
        
def main():
    instructionSetGenerator = InstructionSetGenerator()
    instructionSetGenerator.generateNodeInstructionSetFiles()
        
if __name__=="__main__":
    main()        