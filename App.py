import tkinter as tk
import matplotlib
from matplotlib.backends.backend_tkagg import (
	FigureCanvasTkAgg,
	NavigationToolbar2Tk
)
from matplotlib.figure import Figure

matplotlib.use('TkAgg')

data = {
	'Python': 11.27,
	'C': 11.16,
	'Java': 10.46,
	'C++': 7.5,
	'C#': 5.26
}
languages = data.keys()
popularity = data.values()


class App(tk.Frame):
	def create_widgets(self):
		figure = Figure(figsize=(6, 4), dpi=300)
		figure_canvas = FigureCanvasTkAgg(figure, self)
		NavigationToolbar2Tk(figure_canvas, self)
		# create axes
		axes = figure.add_subplot()
		# create the barchart
		axes.bar(languages, popularity)
		axes.set_title('Top 5 Programming Languages')
		axes.set_ylabel('Popularity')

		figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		self.QUIT = tk.Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["fg"] = "red"
		self.QUIT["command"] = self.quit

		self.QUIT.pack()

	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.pack()
		self.create_widgets()
