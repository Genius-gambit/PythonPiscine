from __future__ import annotations

def square(x: int | float) -> int | float:
	return x * x

def pow(x: int | float) -> int | float:
	return x ** x

def outer(x: int | float, function) -> object:
	count = 0
	def inner() -> float:
		nonlocal x
		result = function(x)
		x = result
		return result
	return inner