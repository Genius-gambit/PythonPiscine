from typing import Any
def ft_statistics(*args: Any, **kwargs: Any) -> None:
	argsList = list(args)
	total = 0
	values = []
	numArgs = 0
	for arg in args:
		numArgs += 1
		total += arg
		values.append(arg)
	if numArgs == 0:
		for value in kwargs.items():
			print("Error")
		return
	
	total = 0
	for arg in argsList:
		total += arg
	mean = total / numArgs
	i = 0
	while i < numArgs - 1:
		j = 0
		while j < numArgs - i - 1:
			if values[j] > values[j + 1]:
				values[j], values[j + 1] = values[j + 1], values[j]
			j += 1
		i += 1
	medianIndex = numArgs // 2
	median = (values[medianIndex - 1] + values[medianIndex]) / 2\
		if numArgs % 2 == 0 else values[medianIndex]
	q1Index = numArgs // 4
	q3Index = q1Index * 3
	quartile = [float(values[q1Index]), float(values[q3Index])]

	SS = 0
	for value in values:
		SS += (value - mean) ** 2
	variance = SS / numArgs
	std = variance ** 0.5
	result = {"mean": mean, "median": median, "quartile": quartile, "std": std, "var": variance}

	for key, value in kwargs.items():
		print(f"{value}: {result[value]}" if value in result else "Error")