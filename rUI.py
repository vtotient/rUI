from cmd import Cmd
import include.strings as strings
from include.device import Device
import include.testCommand as testCommand
from include.logger import logger
import os.path, json
from functools import wraps

# Require Device function decorator. Use this on any method that requires a device to be set
def require_device(func):
    @wraps(func)
    def wrapper(self=None, *arg, **kwargs):
        if self.device.ser.is_open:
            func(self, *arg, **kwargs)
        else:
            print("No device! Please connect to a device with \"connectDevice\"")
    return wrapper


def setLocalOption(data):
    options = {}
    if os.path.isfile("options.json"):
        with open("options.json","r") as f:
            options = json.load(f)
    
    for key, value in data.items():
        options[key] = value
    
    with open("options.json", "w") as f:
        json.dump(options, f)

def getLocalOption(key):
    if os.path.isfile("options.json"):
        with open("options.json","r") as f:
            options = json.load(f)
            return options[key]

    return None

class rUI(Cmd):
    prompt = "rUI> "
    intro = strings.banner  

    device = Device()
    testQueue = []

    def preloop(self):
        if os.path.isfile("options.json"):
            with open("options.json", "r") as f:
                options = json.load(f)

                # Do initialization on options stored in options.json

                # Set last port
                lastPort = getLocalOption('lastPort')
                if lastPort in [i.device for i in self.device.listDevices()]:
                    self.device.setPort(lastPort)
                    self.device.openPort()
                    self.intro += "Connected to last port " + lastPort + "\n"

    def do_exit(self, inp):
        "Exit the rUI"
        print(strings.outro)
        return True

    def do_connectDevice(self, inp):
        """Connect to a serial device.
        Shows list of open devices and prompts selection."""
        logger.info("Listing devices")

        # Get a list of the available serial ports
        self.device.closePort()
        ports = self.device.listDevices() 
        portNames = []
    
        # Get device names and print to screen
        i = 0
        for port in ports:
            logger.info("Device found: %s", port)
            portNames.append(port.device)
            # Format
            print(str(i) + "     " + str(port))
            i = i + 1
        
        # Prompt user to select serial device
        while True:
            selection = input("Enter selection[q(quit)]: ")

            if selection is "q":
                return False
            
            # Verify valid selction 
            try:
                selection = int(selection)
            except:
                print("Invalid option...try again")
                continue
            
            if selection < len(portNames):
                self.device.setPort(portNames[selection])
                self.device.openPort()

                setLocalOption({'lastPort':portNames[selection]})

                logger.info("Selecting device: %s", portNames[selection])
                break
            else:
                print("Selection out of range...try again")

    @require_device
    def do_disconnectDevice(self, inp):
        """Disconnects the current device"""
        self.device.closePort()
        print("Disconnected from "+ self.device.getPort())
        self.device.setPort(None)

        setLocalOption({'lastPort':None})


    @require_device
    def do_listen(self, inp):
        "Read from device"
        # Ensure serial port is open 
        print("Enter CTRL-c to terminate read")
        try:
            while True:
                if True:
                    print(str(self.device.readLine(), 'utf-8'))
        except KeyboardInterrupt:
            print("Read terminated")


    def do_test(self, inp):
        "Handles test"

        try:
            inp = inp.split()
            getattr(testCommand, 'do_'+inp[0])(self," ".join(inp[1:]))
        except AttributeError:
            print("Please enter a valid command")
    
    def help_test(self):
        print("Handles test queue and excecution.")
        testFncNames = [fnc for fnc in dir(testCommand) if len(fnc) > 3 and fnc[:3] == "do_"]
        for fnc in testFncNames:
            print(fnc[3:]+": "+testCommand.__dict__[fnc].__doc__)

    def complete_test(self, text, line, begidx, endidx):
        testCommands = [command[3:] for command in dir(testCommand) if len(command) > 3 and command[:3] == "do_"]
        if text:
            return [ command for command in testCommands if command.startswith(text) ]
        else:
            return testCommands

        
    @require_device
    def do_getSpiState(self, inp):
        "Get SPI State"

        STMReceiveCode = 3 # Integer code that the STM looks for
        self.device.writeInt8(STMReceiveCode)
        state = self.device.readBytes(1)

        states = ["HAL_SPI_STATE_RESET: Peripheral not Initialized",
                    "HAL_SPI_STATE_READY: Peripheral Initialized and ready for use",
                    "HAL_SPI_STATE_BUSY: an internal process is ongoing",
                    "HAL_SPI_STATE_BUSY_TX: Data Transmission process is ongoing",
                    "HAL_SPI_STATE_BUSY_RX: Data Reception process is ongoing",
                    "HAL_SPI_STATE_BUSY_TX_RX: Data Transmission and Reception process is ongoing",
                    "HAL_SPI_STATE_ERROR: SPI error state",
                    "HAL_SPI_STATE_ABORT: Abort state"]

        print("State: "+str(state[0]))
        print(states[state[0]])



logger.info("---Starting rUI---")
# Driver 
p = rUI()
p.cmdloop()

