import serial.tools.list_ports as list_ports
from pyfirmata import INPUT, ArduinoMega, util
from time import sleep

from FileManagement import append_new_data
from State import get_continue_reading
import pandas as pd

# from threading import Event

df = pd.DataFrame(columns=["voltage", "current", "temperature", "frequency"])


class ArduinoConnection:
	def connect_arduino(self):
		ports = list(list_ports.comports(True))
		arduino_port = next(filter(
			lambda p: (p.manufacturer and "Arduino" in p.manufacturer) or "Arduino" in p.description, ports
		), None)
		self.board = ArduinoMega(arduino_port.device)
		print(self.board.get_firmata_version())

	def establish_pins(self):
		self.it = util.Iterator(self.board)
		self.it.start()

		self.arduino_inputs.update(
			voltage=self.board.get_pin("a:0:i"),
			current=self.board.get_pin("a:1:i"),
			temperature=self.board.get_pin("a:2:i"),
			frequency=self.board.get_pin("d:2:i")
		)
		# for k in self.arduino_inputs:
		# 	self.arduino_inputs[k].enable_reporting()

	def read_signals(self):
		new_data = dict(
			voltage=0,
			current=0,
			temperature=0,
			frequency=0
		)

		for parameter in self.arduino_inputs:
			new_data[parameter] = self.arduino_inputs[parameter].read()

		if new_data.get("voltage") is not None:
			append_new_data(new_data)
			print(new_data)

	def __init__(self):
		self.board = None
		self.it = None
		self.connect_arduino()
		self.arduino_inputs = dict()
		self.establish_pins()
		while get_continue_reading():
			self.read_signals()
			sleep(2)
		# for x in range(20):
		# 	self.board.digital[13].write(1)
		# 	sleep(1)
		# 	self.board.digital[13].write(0)
