from load_csv import load
import matplotlib.pyplot as plt

def	main():
	data = load("data.csv")
	countryData = data[data['country'] == 'United Arab Emirates']
	years = countryData.columns[1:]
	lifeExpectancy = countryData.values[0][1:]

	plt.plot(years, lifeExpectancy, label='UAE')
	plt.title('Life Expectancy in UAE Over the Years')
	plt.xlabel('Year')
	plt.xticks(years[::40], rotation=45)
	plt.ylabel('Life Expectancy')
	plt.yticks(range(30, 101, 10))
	plt.legend()
	plt.tight_layout()
	plt.show()

if __name__ == '__main__':
	main()