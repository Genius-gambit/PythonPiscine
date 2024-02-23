import os
import pandas as pd

def	load(path: str) -> pd.DataFrame:
	try:
		if not os.path.exists(path):
			raise AssertionError("The file doesn't exist")
		if not path.lower().endswith('.csv'):
			raise AssertionError("The file format is not .csv")
		dataset = pd.read_csv(path)
		print(f"Loading dataset of dimensions {dataset.shape}")
		return dataset
	except AssertionError as error:
		print(AssertionError.__name__ + ":", error)
		return None

if __name__ == '__main__':
	print(load('data.csv'))