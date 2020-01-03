# KEEPS TRACK OF HOW MANY TIMES EQUIVALENT VALUES ARE ADDED.

# 'Counter' class comes from the 'collections' module in Python3.
# 'Collections' module provides user with specialized container datatypes,
# providing an alternative to Python's built-in containers such as lists,
# dictionaries, and tuples.
import collections

# Supports 3 forms of initialization
# 1 - sequence of items
print collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])

# 2 - dictionary containing keys and counts
print collections.Counter({'a':2, 'b':3, 'c':1})

# 3 - keyword arguments mapping string names to counts
print collections.Counter(a=2, b=3, c=1)

# Empty counter can be constructed with no arguments and populated via
# the update() method
c = collections.Counter()
print 'Initial: ',c

c.update('abcdaab')
print 'Sequence: ',c

c.update({'a':1, 'd':5})
print 'Dict: ',c

# Once a counter is populated, its values can be retrieved using the 
# dictionary API
# Counter does not raise error for unknown items. If value has not been
# seen in the input, its count is 0
c = collections.Counter('abcdaab')

for letter in 'abcde':
    print '%s : %d' % (letter, c[letter])


# elements() method returns an iterator that produces all of the items known
# to the Counter
c = collections.Counter('extremely')
c['z'] = 0
print c
print list(c.elements())

# most_common() method produces a sequence of the n most frequently encountered
# input values and their respective counts
c = collections.Counter()
with open('/usr/share/dict/words', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

print 'Most common: '
for letter, count in c.most_common(3):
    print '%s: %7d' % (letter, count)

# Counter supports arithmetic and set operations for aggregating results
c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print '\nC1: ',c1
print 'C2: ',c2

print '\nCombined counts: '
print c1 + c2

print '\nSubtraction: '
print c1 - c2

print '\nIntersection (taking positive minimums): '
print c1 & c2

print '\nUnion (taking maximums): '
print c1 | c2

