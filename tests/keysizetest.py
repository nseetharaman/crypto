import base64

#Pass
def hammingDist (s1, s2):
	#assert len(s1) == len(s2)
	s1 = ''.join(format(ord(x), '08b') for x in s1)
	s2 = ''.join(format(ord(x), '08b') for x in s2)
	return sum(c1 != c2 for c1,c2 in zip(s1,s2))

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

#Pass
f = open('../6.txt', 'r')
ct = f.read().decode("base64")
#print len(ct)

best_keysize = 0
smallest_nhd = 100

#Pass
def findKeySize():
	smallest_mean_nhd = 99999
	best_KEYSIZE = 0
	KEYSIZE = 1
	while KEYSIZE <= 40:
		chunks = list(chunkstring(ct, KEYSIZE*2))
		numchunks = len(chunks)
		hamsum = 0
		mean_nhd = 0
		for chunk in chunks:
			chunklow = chunk[:(len(chunk)/2)]
			chunkhigh = chunk[(len(chunk)/2):]
			hd = hammingDist(chunklow, chunkhigh)
			nhd = float(hd)/float(KEYSIZE)
			hamsum += nhd
		mean_nhd = hamsum/numchunks
		if mean_nhd < smallest_mean_nhd:
			smallest_mean_nhd = mean_nhd
			best_KEYSIZE = KEYSIZE
		KEYSIZE += 1
	return best_KEYSIZE

print findKeySize()


#5, 3, 2, 7, 
