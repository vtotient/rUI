import serial
from serial.tools import list_ports
import select

class Device():
	# Define device parameters
	baudrate = 115200
	port = None
	timeout = 5000	
	ser = None

	MAXSIZE = 100

	def __init__(self):
		self.ser = serial.Serial()
		self.ser.baudrate = self.baudrate
		self.ser.timeout = self.timeout

	def setPort(self, portName):
		self.ser.port = portName

	def openPort(self):
		self.ser.open()
		return self.ser.is_open

	def closePort(self):
		self.ser.close()
		return self.ser.is_open

	def getPort(self):
		return self.ser.port

	def isOpen(self):
		return self.ser.is_open

	def readLine(self):
		return self.ser.readlines()

	def listDevices(self):
		return list_ports.comports()

	def readBytes(self, n):
		return self.ser.read(n)

	def writeBytes(self, data):
		if len(data) > self.MAXSIZE:
			return False
		self.ser.write(data)

	def writeInt8(self, data):
		return self.writeBytes(data.to_bytes(1, 'little'))
