class BaseTest(object):
    #Define basetest parameters
    name = None
    duration = 1000
    def _init_(self):
        pass
    
    def run(self):
        # Ensure device is plugged in
        print("Kicking off the test")

    def terminate(self):
        raise NotImplementedError()
    
    def name(self, testName):
        self.name = testName
    
    def getName(self):
        return self.name
    
    def duration(self, length):
        self.duration = length
    
    def getDuration(self):
        return self.duration

class DummyTest1(BaseTest):
    name = "dummytest1"
    duration = 1000
    def _init_(self):
        super._init_()
    
    def run(self):
        super.run()
    
    def name(self, testName):
        self.name = testName
    
    def getName(self):
        return self.name
    
    def duration(self, length):
        self.duration = length
    
    def getDuration(self):
        return self.duration


