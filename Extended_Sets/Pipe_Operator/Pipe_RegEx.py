import re

pattern = re.compile("^(log|ply)wood$")

for i, line in enumerate(open('regex24.txt')):
	for match in re.finditer(pattern, line):
		print 'found on line %s: %s:' %(i+1, match.group())
