from abc import ABC, abstractmethod

class Character(ABC):
	
	@abstractmethod
	def	__init__(self, first_name, family_name, is_alive=True) -> None:
		self.first_name = first_name
		self.is_alive = is_alive
		self.family_name = family_name
	
	def	die(self):
		pass

	def	__str__(self) -> str:
		return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
	
	def	__repr__(self) -> str:
		return self.__str__()

class Stark(Character):
	"""Your docstring for Class"""
	def	__init__(self, first_name, is_alive=True) -> None:
		"""Your docstring for Constructor"""
		self.first_name = first_name
		self.is_alive = is_alive

	def	die(self):
		"""Your docstring for Method"""
		self.is_alive = False