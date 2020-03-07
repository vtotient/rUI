from .baseTest import BaseTest

class DummyTest1(BaseTest):
    duration = 1000
    def __init__(self, device, duration=0, arg1="cat", **kwargs):
        # Pass arguments that werent explicitly defined to parent class
        # Set up device in parent class
        super().__init__(device, **kwargs) 
        self.setDuration(duration)
    
    def run(self):
        super().run()
        self.device.writeInt8(self.duration)
        print(self.device.readBytes(1))
    
    def setName(self, testName):
        self.name = testName
    
    def getName(self):
        return self.name
    
    def setDuration(self, length):
        self.duration = length
    
    def getDuration(self):
        return self.duration

    def __repr__(self):
        return self.name + " -- duration: " + str(self.duration) + " " + hex(self.opcode)

    def __str__(self):
        return self.__repr__()


