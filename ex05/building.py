import argparse
import sys

def	calcString(_str):
	upperCaseLetters = 0
	lowerCaseLetters = 0
	digits = 0
	spaces = 0
	punctuations = 0
	for i in _str:
		if i.isupper():
			upperCaseLetters += 1
		elif i.islower():
			lowerCaseLetters += 1
		elif i.isdigit():
			digits += 1
		elif i.isspace() or i == '\r' or i == '\n':
			spaces += 1
		else:
			punctuations += 1
	print("The text contain " + str(len(_str)) + " letters")
	print(str(upperCaseLetters) + " upper letters")
	print(str(lowerCaseLetters) + " lower letters")
	print(str(punctuations) + " punctuation marks")
	print(str(spaces) + " spaces")
	print(str(digits) + " digits")

def main():
	parser = argparse.ArgumentParser(prog='ProgramName')
	parser.add_argument('string', help='An optional argument')

	_list = sys.argv
	if len(_list) == 1:
		user_input = input("What is the text to count?\n")
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
