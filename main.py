import sys
import copy

def createCharCountMap(str1):
	return {s:str1.count(s) for s in set(str1)}

def sortMapByCounts(d):
	return {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

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
		print("false")
	else:
		print("true")

	
s1 = sys.argv[1]
s2 = sys.argv[2]

u1 = len(set(s1))
u2 = len(set(s2))

if(u1 == u2):
	if len(s1) > len(s2):
		print('false')
	else:
		checkOneOnOneMapping(sortMapByCounts(createCharCountMap(s1)), sortMapByCounts(createCharCountMap(s2)))
elif(u1 < u2):
	if len(s1) >= len(s2):
		print('false')
	else:
		checkOneOnOneMapping(sortMapByCounts(createCharCountMap(s1)), sortMapByCounts(createCharCountMap(s2)))
else:
	if len(s1) <= len(s2):
		print('true')
	else:
		print('false')