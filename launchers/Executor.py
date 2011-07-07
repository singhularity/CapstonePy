from threading import  Thread
import time
class Executor(Thread):
    def __init__(self, numberOfNodes, algorithm):
        Thread.__init__(self)
        self.numberOfNodes = numberOfNodes
        self.algorithm = algorithm
        self.instructionSet = None
        self.times = []
        
    def setInstructionSet(self, instructionSet):
        self.instructionSet = instructionSet
    
    def getTimes(self):
        return self.times
    
    def run(self):
        for nextInst in self.instructionSet:
            startTime = time.clock()
            self.algorithm.readContent(int(nextInst.nodeNum) - 1, nextInst.content) 
            endTime = time.clock() - startTime
            self.times.append(endTime)
        print self.times