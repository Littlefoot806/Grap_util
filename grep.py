import argparse
import re
import sys


def main():
	''' Command line utility that finds input lines that meet
		specified regular expression, and displays them
	'''
	parser = argparse.ArgumentParser()
	parser.add_argument("-v", "--ignore", action="store_true", help="If True, find all, except for expression")
	parser.add_argument('expression', type=str, help='What is the expression?')
	parser.add_argument('file', type=argparse.FileType('r'), help='Path to the file')

	args = parser.parse_args()

	# Regex check
	regex = False
	for i in args.expression:
		if i in r'.^$*+?{[\|(':
			args.expression = r''.join(args.expression)
			regex = True
			break

	# Output generation
	output_gen = findMatchesInFile(args.expression, args.file, args.ignore, regex)
	
	# Outputting
	if output_gen:
		for line in output_gen:
			sys.stdout.write(line)
	else:
		sys.stdout.write('No have a matches')

def findMatchesInFile(expression, file, ignore=False, regex=False):
	''' Reading a file and finding matches with expression '''
	for line in file:
		if regex:
			matches = re.match(expression, line)
			if matches and ignore == False:
				yield line
			elif matches is None and ignore:
				yield line
		else:
			if expression not in line and ignore:
				yield line
			if expression in line and ignore == False:
				yield line
			

if __name__ == '__main__':
	main()