import fileinput
import re

#regex29.txt
for line in fileinput.input():
	line = re.sub(r'([A-Z a-z]{3})\s([0-9]+)[a-z]+\s[0-9]{2}([0-9]{2})', r'\2-\1-\3', line.rstrip())
	print(line)
