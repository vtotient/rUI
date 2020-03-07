from cmd import Cmd
import include.strings as strings
from include.device import Device
from include.logger import logger
import os.path, json
from functools import wraps

"""Radio User Interface for testing.

Overall description of the program. Include brief description of exported classes and functions and/or usage
examples?

"""

def require_device(func):
	"""Function decorator. 

	Use for any method that requires a device to be set.

	"""

	@wraps(func)
	def wrapper(self=None, *arg, **kwargs):
		"""Wraps device.

    	Args:
        	*arg: An open Bigtable Table instance.
        	**kwargs: A sequence of strings representing the key of each table row
            to fetch.

    	Returns:
        	wrapper

        	If device.ser can find no open device,
        	then prints error message. 
        """

		if self.device.ser.is_open:
			func(self, *arg, **kwargs)
		else:
			print("No device! Please connect to a device with \"connectDevice\"")
	return wrapper


def setLocalOption(data):
	"""local option setter

	Args:
		data

	"""

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

	def preloop(self):
		if os.path.isfile("options.json"):
			with open("options.json", "r") as f:
				options = json.load(f)

				# Do initialization on options stored in options.json

				
				lastPort = getLocalOption('lastPort') # Set last port
				if lastPort in [i.device for i in self.device.listDevices()]:
					self.device.setPort(lastPort)
					self.device.openPort()
					self.intro += "Connected to last port " + lastPort + "\n"

	def do_exit(self, inp):
		"Exit the rUI"
		print(strings.outro)
		return True

	def do_connectDevice(self, inp):
		"""Connect to a serial device

		Args:
			inp

		"""

		logger.info("Listing devices") # Get a list of the available serial ports
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
		"Disconnect current device"
		self.device.closePort()
		print("Disconnected from "+ self.device.getPort())
		self.device.setPort(None)

		setLocalOption({'lastPort':None})

	@require_device
	def do_listen(self, inp):
		"""Read from device. First ensure serial port is open.

		Args:
			inp

		Returns:

		Raises:
			KeyboardInterrupt

		"""
	
		print("Enter CTRL-c to terminate read")
		try:
			while True:
				if True:
					print(str(self.device.readLine(), 'utf-8'))
		except KeyboardInterrupt:
			print("Read terminated")

	@require_device
	def do_getSpiState(self, inp):
		"""Get SPI State

		Args:
			inp

		Returns:
			Prints state associated with inp
		"""

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


	@require_device
	def do_getState(self, inp) :
	    
	    ArduinoReceiveCode = 1 # Integer code that the arduino looks for
	    
	    #dictionary
	    states = {0: "State0", 
	    			1: "State1", 
	    			2: "State2",
	    			3: "State3"} 

	    self.device.writeInt8(ArduinoReceiveCode)
	    byteReturned = self.device.readBytes(1)

	    print("State: " + states.get(byteReturned))



logger.info("---Starting rUI---")
# Driver 
p = rUI()
p.cmdloop()

