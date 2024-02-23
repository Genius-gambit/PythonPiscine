from load_csv import load
import matplotlib.pyplot as plt

def	preprocessPopulation(popStr: str):
	if popStr.endswith("M"):
		return float(popStr[:-1]) * 1e6
	elif popStr.endswith("k"):
		return float(popStr[:-1]) * 1e3
	else:
		return float(popStr)

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

	uaePop = [preprocessPopulation(pop) for pop in uaePop]
	francePop = [preprocessPopulation(pop) for pop in francePop]
	hungaryPop = [preprocessPopulation(pop) for pop in hungaryPop]

	plt.plot(years, uaePop, label=campus)
	plt.plot(years, francePop, label=country)
	plt.plot(years, hungaryPop, label=home)

	plt.title("Population in {}, {} and {}".format(campus, country, home))
	plt.xlabel("Year")
	plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
	plt.xlim(1800, 2040)
	plt.ylabel("Population")
	plt.legend()
	plt.tight_layout()
	maxPop = max(max(uaePop), max(francePop), max(hungaryPop))
	y_ticks = [i * 1e7 for i in range(int(maxPop / 1e7) + 1)]
	plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
	plt.show()

if __name__ == '__main__':
	main()