import pandas as pd

# def retrieve_data(data_path):
#     df = pd.read_csv(data_path)


class Graphic:

	def __init__(self, data_path):
		self.path = data_path
		print(self.path)
