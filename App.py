import tkinter as tk
import matplotlib
from matplotlib.backends.backend_tkagg import (
	FigureCanvasTkAgg,
	NavigationToolbar2Tk
)
from matplotlib.figure import Figure
import FileManagement


matplotlib.use('TkAgg')

# data = {
# 	'Python': 11.27,
# 	'C': 11.16,
# 	'Java': 10.46,
# 	'C++': 7.5,
# 	'C#': 5.26
# }
# languages = data.keys()
# popularity = data.values()


class App(tk.Frame):
	def create_widgets(self):
		parameters = ["voltage", "current", "temperature", "frequency"]
		for parameter in parameters:
			figure = Figure(figsize=(3, 2), dpi=150)
			figure_canvas = FigureCanvasTkAgg(figure, self)
			toolbar = NavigationToolbar2Tk(figure_canvas, self, pack_toolbar=False)
			data = FileManagement.get_data()
			# create axes
			voltage_axes = figure.add_subplot()
			voltage_axes.plot(data[parameter])
			voltage_axes.set_title(parameter)
			figure_canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.pack()
		self.create_widgets()
