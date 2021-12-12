import re

test_input = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

line = "light salmon bags contain 5 wavy plum bags, 4 drab white bags, 5 muted bronze bags, 5 mirrored beige bags."
# \w+ matches one or more words
# the first capture group matches (light salmon)
# the second capture group grabs the rest of the string
parent, entries = re.match(r'(\w+ \w+) bags contain (.*)', line).groups()
# \d+ matches one or more integers (could be two digit integers, for example)
# The bags? is optional
print([[int(e.groups()[0]), e.groups()[1]] for e in re.finditer(r'(\d+) (\w+ \w+) bags?', entries)])
