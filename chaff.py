import random
import hashlib

def hash(inp):
	a = hashlib.md5()
	a.update(inp)
	hazh = a.hexdigest()
	
	cache = []
	timez = random.randint(20,100)
	for i in range(timez):
		b = hashlib.md5()
		rand = random.randint(1000000,9999999)
		b.update(str(rand))
		e = b.hexdigest()
		cache.append(e)
	l = len(cache)
	place = random.randint(0,l-1)
	cache[place] = hazh
	for i in range(l-1):
		print str(i) + ":" + cache[i]
	
	print "Your hash is #%s" % place

rea = raw_input("Enter a hash: ")
hash(rea)
