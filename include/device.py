import serial
from serial.tools import list_ports
import select

class Device():
	# Define device parameters
	baudrate = 115200
	port = None
	timeout = 5000	
	ser = None

	def __init__(self):
		self.ser = serial.Serial()
		self.ser.baudrate = self.baudrate
		self.ser.timeout = self.timeout

	def setPort(self, portName):
		self.ser.port = portName

	def openPort(self):
		self.ser.open()
		return self.ser.is_open

	def isOpen(self):
		return self.ser.is_open

	def readLine(self):
		return self.ser.readlines()

	def listDevices(self):
		return list_ports.comports()
