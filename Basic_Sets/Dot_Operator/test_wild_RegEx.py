import re

pattern = re.compile("fooa*bar")

for i, line in enumerate(open('regex01.txt')):
	for match in re.finditer(pattern, line):
            print("found on line %s: %s:" % (i+1, match.group()))
