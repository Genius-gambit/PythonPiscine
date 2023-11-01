import argparse
import sys

def	calcString(str):
	upperCaseLetters = 0
	lowerCaseLetters = 0
	digits = 0
	spaces = 0
	punctuations = 0
	for i in str:
		if i.isupper():
			upperCaseLetters += 1
		elif i.islower():
			lowerCaseLetters += 1
		elif i.isdigit():
			digits += 1
		elif i.isspace():
			spaces += 1
		else:
			punctuations += 1
	print(upperCaseLetters)
	print(lowerCaseLetters)
	print(digits)
	print(spaces)
	print(punctuations)

def main():
	parser = argparse.ArgumentParser(prog='ProgramName')
	parser.add_argument('string', help='An optional argument')

	_list = sys.argv
	if len(_list) == 1:
		user_input = input("")
		__name__ = '__calcString__'
		if __name__ == '__calcString__':
			calcString(user_input)
		return
	assert len(_list) <= 2, "More than one argument is provided"
	args = parser.parse_args()
	print(args.string)
	__name__ = '__calcString__'
	if __name__ == '__calcString__':
		calcString(str(args.string))

if __name__ == '__main__':
    main()
