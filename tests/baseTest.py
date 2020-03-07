TESTS_DIR = "tests/"
class BaseTest(object):
    #Define basetest parameters
    name = None
    duration = 1000
    opcode = 0xFF

    # When an __init__ is called on the BaseTest class, a child should be
    # provided to know which test is really being instanciated. `**kwargs` are
    # any arguments that were not explicitly defined by the constructor of both
    # the child class and this class. If these arguments exist, throw an error
    # because unused information was provided.
    def __init__(self, device, **kwargs):
        # Set name to class' name
        self.name = self.__class__.__name__
        if len(kwargs) != 0 and self:
            raise NameError("Unknown arguments for " + self.name, kwargs)
        self.device = device

        # Get opcode
        with open(TESTS_DIR+"opcodes.csv") as file:
            for line in file.readlines():
                cols = line.split(",")
                if cols[3] == self.name:
                    self.opcode = int(cols[2])
                    break

    
    def run(self):
        # Ensure device is plugged in
        print("Kicking off the test")
        self.device.write8Int(self.opcode) # Send the opcode

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
