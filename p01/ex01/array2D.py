import numpy as np

def	slice_me(family: list, start: int, end: int) -> list:
	"""

	Array is passed to this function along with two int values which
	is the starting and ending of the list. The function is used to create
	a new list which will have the range of the list from start to end and
	return it

	Args: family: list, start: int, end: int

	Return Values: List type
	
	"""
	try:
		if not isinstance(family, list) \
				or not isinstance(start, int) or not isinstance(end, int):
			raise AssertionError("Input must be a list and 2 integers.")
		if not all(len(item) == len(family[0]) for item in family):
			raise AssertionError("Input list with different sizes.")
		print(f"My shape is : {np.array(family).shape}")
		print(f"My new shape is : {np.array(family)[start:end].shape}")
		return np.array(family)[start:end].tolist()
	except AssertionError as error:
		print("\033[31m", AssertionError.__name__ + ":", error, "\033[0m")
		return ""
	
if	__name__ == '__main__':
	"""

	Test Cases
	
	"""
	family = [[1.80, 78.4],
			[2.15, 102.7],
			[2.10, 98.5],
			[1.88, 75.2]]
	print("\n      TEST 1\n")
	print(slice_me(family, 0, 2))
	print("\n      TEST 2\n")
	print(slice_me(family, 1, -2))
	print("\n      TEST 3\n")
	family = 10
	print(slice_me(family, 0, 2))
	print("\n      TEST 4\n")
	family = [[1.80, 78.4],
			[2.15, 102.7],
			[2.10, 98.5, 2.15],
			[1.88, 75.2]]
	print(slice_me(family, 0, 2))
	print("\n      TEST 5\n")
	family = [[1.80, 78.4],
			[2.15, 102.7],
			[2.10, 98.5],
			[1.88, 75.2]]
	print(slice_me(family, "a", 2))