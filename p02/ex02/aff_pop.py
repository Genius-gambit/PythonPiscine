from load_csv import load
import matplotlib.pyplot as plt

def	main():
	data = load("data.csv")

	campus = 'United Arab Emirates'
	country = 'France'
	home = 'Hungary'

	uaeData = data[data['country'] == campus].iloc[:, 1:]
	franceData = data[data['country'] == country].iloc[:, 1:]
	hungaryData = data[data['country'] == home].iloc[:, 1:]

	uaePop = uaeData.values.flatten()
	francePop = franceData.values.flatten()
	hungaryPop = hungaryData.values.flatten()
	years = uaeData.columns.astype(int)

if __name__ == '__main__':
	main()