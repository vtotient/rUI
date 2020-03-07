from cmd import Cmd
import include.strings as strings
from include.device import Device
from include.logger import logger
import os.path, json
from functools import wraps
from abc import ABC 
from abc import ABCMeta

class BaseTest(ABC):
    """Defines what IS a test. 

    Includes methods and variables that every test object should have. 
    Uses the abstract base class (abc) module.
    @abstractmethod decorator used on methods that user needs to define.
    All other methods will be inherited and already implemented.

    """

    def __init__(self):
        self.name = None 
        self.timeout = 1000

    @abstractmethod
    def set_name(self):
        pass

    def setup(self):
        pass
    
    def teardown(self):
        pass

    @abstractmethod
    def run(self)
        print "Running" name

    def terminate():
        print name "terminated"

# Note: Unlike Java abstract methods, the abstract methods defined in BaseTest may have an implementation. 
# This implementation can be called via the super() mechanism from the class that overrides it. 
# This could be useful as an end-point for a super-call in a framework that uses cooperative multiple-inheritance.