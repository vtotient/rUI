from .baseTest import BaseTest

class DummyTest1(BaseTest):
    name = "dummytest1"
    duration = 1000
    def __init__(self, device, duration=0, arg1="cat", **kwargs):
        super().__init__(self, device, **kwargs) # Pass arguments that werent explicitly defined to parent class
        self.setDuration(duration)
        self.device = device
    
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
        return self.name + " -- duration: " + str(self.duration)

    def __str__(self):
        return self.__repr__()


