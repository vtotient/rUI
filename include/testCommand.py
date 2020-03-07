import yaml
# import logger
import sys
sys.path.append('../')

TESTPLAN_DIR = "testplans/"

from rUI import require_device
import tests


def do_add(self, inp):
    "Add a test file to the queue"
    
    args = inp.split()

    addToQueueFromFile(self, TESTPLAN_DIR+args[0]) # self (for testQueue variable), and filename


def addToQueueFromFile(self, fileName):
    try:
        with open(fileName,'r') as file:
            tempQueue = [] # Add tests to a temp queue in case an error occurs to easily abort all additions
            y = yaml.load_all(file, Loader=yaml.Loader) # Open yaml
            for test in y:
                testName = list(test.keys())[0] # Get the name of the test

                # Retrieve the test object from test files and instantiate with args from yaml
                testObject = getTest(testName)(self.device, **test[testName]) 
                
                tempQueue.append(testObject) # add to temp queue
            
            # Push temp queue onto testQueue
            self.testQueue += tempQueue
            for testObject in tempQueue:
                print("Added", testObject.name, "to queue.")

    except FileNotFoundError:
        print("File not found. Try again.")
    except NameError as e: # In case extra arguments were provided that shouldn't've been
        print("NameError", e)
        print("Did not add anything to queue.")


def getTest(testName):
    "Returns test object from tests folder"

    if testName in dir(tests):
        # Retrieves a given test class from the tests module
        # NOTE: Since each test class is part of a sub module of the tests
        # module, we must use getattr once to get the sub module and a second
        # time to get the class.
        return getattr(getattr(tests, testName), testName)
    else:
        pass
        # logger.warning("Test "+testName+" not found")


def do_list(self, inp):
    "List the currently queued tests."

    if not self.testQueue:
        print("The test queue is empty")
        return
    for i, testObject in enumerate(self.testQueue):
        print("["+str(i)+"]",testObject)

def do_remove(self, inp):
    """Remove a test
    Args:
        testNumber: test number from `listTests` to remove
        `-f`: Force remove/skip confirmation
    Example:  
        rUI> test remove -f 2
        Removed test2 from the queue."""
    inp = inp.split()
    if len(inp) < 1:
        print("Please input a test number")
        return
    try:
        # If the test should forcibly removed, dont confirm
        if inp[0] != '-f':
            toRemoveIndex = int(inp[0])
            ans = input("Are you sure you would like to remove "+str(self.testQueue[toRemoveIndex])+" from the testQueue (Y/n)? ")
            if not (ans.lower() == "y" or ans.lower() == "yes" or ans.lower() == ""):
                print("Canceling...")
                return
        else:
            toRemoveIndex = int(inp[1])
        print("Removed", self.testQueue.pop(toRemoveIndex),"from queue.")
    except ValueError:
        # If an invalid test number (out of range) to remove is provided
        print("Please input a valid test number")

@require_device
def do_run(self, inp):
    """Runs a test. Excecute test plan outlined by queue if no\n      test number specified.
    Args:
        testNumber (optional): test number from `listTests` to remove
    """

    if inp:
        try:
            print("Running test",self.testQueue.pop(int(inp)))
        except IndexError:
            print("Please enter a valid queue index.")
            return
    else:
        print("Excecuting test plan:")
        while len(self.testQueue) > 0:
            print("Running test",self.testQueue[0])
            self.testQueue.pop(0).run() # Remove the test from the queue, and run it.


