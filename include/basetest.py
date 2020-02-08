from cmd import Cmd
import include.strings as strings
from include.device import Device
from include.logger import logger
import os.path, json
from functools import wraps
from abc import ABC 
from abc import ABCMeta

# Using the abc (abstract base class) module 
# abc BaseTest defines some methods that every test should have

class BaseTest(ABC):

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

# want @abstractmethod decorator on methods that user needs to define
# All  other methods will be inherited and already implemented.