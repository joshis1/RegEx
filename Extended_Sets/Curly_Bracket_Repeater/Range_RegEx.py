import re

pattern = re.compile("^[0-9]{3}$")

for i, line in enumerate(open('regex18.txt')):
	for match in re.finditer(pattern, line):
		print 'found on line %s: %s:' %(i+1, match.group())
