import os
import csv
import pandas as pd

file_path = os.getcwd() + "/Data.csv"
cols = ["voltage", "current", "temperature", "frequency"]

if not os.path.exists(file_path):
	with open(file_path, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(cols)

file_w = open(file_path, "at")
dw = csv.DictWriter(file_w, cols)
df = None


def get_data():
	global df
	if df is None:
		df = pd.read_csv(file_path)
	return df


def append_new_data(data):
	dw.writerow(data)
	global df
	if df is not None:
		df.append(data, ignore_index=True)
