from cmd import Cmd
import include.strings as strings
from include.device import Device

class rUI(Cmd):
	prompt = "rUI> "
	intro = strings.banner	

	device = Device()

	def do_exit(self, inp):
		"Exit the rUI"
		print(strings.outro)
		return True

	def do_connectDevice(self, inp):
		"Connect to a serial device"
		# Get a list of the available serial ports
		ports = self.device.listDevices() 
		portNames = []
	
		# Get device names and print to screen
		i = 0
		for port in ports:
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
				break
			else:
				print("Selection out of range...try again")

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



# Driver 
p = rUI()
p.cmdloop()

