class calculator:
	def	__init__(self, vector) -> None:
		self.vector = vector

	def __add__(self, object) -> None:
		self.vector = [x + object for x in self.vector]
		print(self.vector)
		return [x for x in self.vector]

	def __mul__(self, object) -> None:
		self.vector = [x * object for x in self.vector]
		print(self.vector)
		return [x for x in self.vector]

	def __sub__(self, object) -> None:
		self.vector = [x - object for x in self.vector]
		print(self.vector)
		return [x for x in self.vector]

	def __truediv__(self, object) -> None:
		try:
			if object == 0:
				raise ZeroDivisionError("Division by Zero is not allowed.")
			self.vector = [x / object for x in self.vector]
			print(self.vector)
			return [x for x in self.vector]
		except ZeroDivisionError as error:
			print(ZeroDivisionError.__name__ + ":", error)