import Launcher
from algorithms import GreedyForwardingCachingAlgorithm

class GreedyForwardingLauncher:
    CLASSNAME = "GreedyForwarding"
    
    def configureAndLaunch(self,host, port):
        launcher = Launcher.Launcher()
        launcher.setParams(host, port)
        algorithm = GreedyForwardingCachingAlgorithm.GreedyForwardingCachingAlgorithm(launcher.nodeRamCapacity, launcher.server)
        launcher.launch(algorithm, launcher.CLASSNAME)
    
def main(args):
    GreedyForwardingLauncher().configureAndLaunch(args[0], args[1])
    
if __name__ == "__main__":
    main(["localhost", "9090"])        