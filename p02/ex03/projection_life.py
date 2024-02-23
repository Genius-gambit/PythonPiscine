from load_csv import load
import matplotlib.pyplot as plt

def	main():
	certified_42 = "income_per_person.csv"
	incomeData = load(certified_42)
	lifeExpectancyData = load("life_expectancy.csv")
	year_1900_column = '1900'
	gnp_1900 = incomeData[year_1900_column]
	lifeExpectancy_1900 = lifeExpectancyData[year_1900_column]
	plt.figure(figsize=(10, 6))
	plt.scatter(gnp_1900, lifeExpectancy_1900)
	plt.title("Life expectancy vs Gross Domestic product (Year 1900)")
	plt.xlabel("Gross Domestic Product")
	plt.ylabel("Life Expectancy (Years)")
	plt.xscale("log")
	plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
	plt.tight_layout()
	plt.show()

if __name__ == '__main__':
    main()