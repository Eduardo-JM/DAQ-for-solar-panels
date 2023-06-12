import tkinter as tk
from ArduinoConnection import ArduinoConnection
from App import App
from threading import Thread
from State import stop_reading

global app
global arduino


def on_closing():
	stop_reading()
	app.join()
	root.destroy()
	arduino.join()


if __name__ == '__main__':
	global app, arduino

	arduino = Thread(target=ArduinoConnection)
	arduino.start()

	root = tk.Tk()
	root.geometry('600x400')
	root.title("Sistema de adquisición de datos")
	root.protocol("WM_DELETE_WINDOW", on_closing)
	app = Thread(target=App, args=[root])
	app.start()
	root.mainloop()
