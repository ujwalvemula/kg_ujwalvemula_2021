import sys
import copy

#method to create a dictionary with character counts
def createCharCountMap(str1):
	return {s:str1.count(s) for s in set(str1)}

#method to sort a dictionary based on values
def sortMapByCounts(d):
	return {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

#method to check for one-on-one mapping
def checkOneOnOneMapping(d1, d2):
	d = copy.copy(d1)
	for k1 in d1:
		if len(d2) == 0:
			break
		for k2 in d2:
			if d1[k1] <= d2[k2]:
				del d[k1]
				del d2[k2]
				break
	if len(d)!=0:
		print('false')
	else:
		print('true')

#reading command line arguments
s1 = sys.argv[1]
s2 = sys.argv[2]

#finding number of unique characters in both the stings
u1 = len(set(s1))
u2 = len(set(s2))


if(u1 >= u2):
	if len(s1) > len(s2):
		#testcase: s1 - 'barr', s2 - 'foe' : false
		#testcase: s1 - 'bard', s2 - 'foe' : false
		print('false')
	else:
		#testcase: s1 - 'bar', s2 - 'fooe' : true
		#testcase: s1 - 'bar', s2 - 'foe' : true
		#testcase: s1 - 'bar', s2 - 'foo' : true
		#testcase: s1 - 'barr', s2 - 'foooo' : true
		print('true')
elif(u1 < u2):
	if len(s1) >= len(s2):
		#testcase: s1 - 'foo', s2 - 'bar' : false
		#testcase: s1 - 'fooo', s2 - 'bar' : false
		print('false')
	else:
		#testcase: s1 - 'foo', s2 - 'barr' : true
		#testcase: s1 - 'fooo', s2 - 'baarr' : false
		checkOneOnOneMapping(sortMapByCounts(createCharCountMap(s1)), sortMapByCounts(createCharCountMap(s2)))
