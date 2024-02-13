import argparse
import sys

def main():
	parser = argparse.ArgumentParser(prog='ProgramName')
	parser.add_argument('number', help='An optional argument')

	_list = sys.argv
	if len(_list) == 1:
		return
	assert len(_list) == 2, "More than one argument is provided"
	args = parser.parse_args()
	assert args.number.lstrip('-+').isdigit() == True, "argument is not an integer"
	number = int(args.number)
	if number % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")

if __name__ == '__main__':
    main()
