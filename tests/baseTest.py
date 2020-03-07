class BaseTest(object):
    #Define basetest parameters
    name = None
    duration = 1000

    # When an __init__ is called on the BaseTest class, a child should be
    # provided to know which test is really being instanciated. `**kwargs` are
    # any arguments that were not explicitly defined by the constructor of both
    # the child class and this class. If these arguments exist, throw an error
    # because unused information was provided.
    def __init__(self, device, child=None, **kwargs):
        if len(kwargs) != 0 and child:
            raise NameError("Unknown arguments for " + child.name, kwargs)
        self.device = device
    
    def run(self):
        # Ensure device is plugged in
        print("Kicking off the test")

    def terminate(self):
        raise NotImplementedError()
    
    def setName(self, testName):
        self.name = testName
    
    def getName(self):
        return self.name
    
    def setDuration(self, length):
        self.duration = length
    
    def getDuration(self):
        return self.duration
