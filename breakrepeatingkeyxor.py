import base64
import collections
import binascii

'''
def calc_str_score(s):
	# Count total letter in input string
	s = s.lower()
	letters = collections.Counter(s)
	most_common = letters.most_common()
	mc_array = []
	for k,v in most_common:
	    if k != ' ':
	        k = k.lower()
	        mc_array.append(k)
	#print mc_array

	topfivestring = str(mc_array[0]+mc_array[1]+mc_array[2]+mc_array[3]+mc_array[4]+mc_array[5]+mc_array[6]+mc_array[7]+mc_array[8]+mc_array[9]+mc_array[10])

	#print topfivestring

	score = 0

	if 'e' in topfivestring:
	    score += 1
	if 'a' in topfivestring:
	    score += 1
	if 't' in topfivestring:
	    score += 1
	if 'o' in topfivestring:
	    score += 1
	if 'n' in topfivestring:
	    score += 1
	if 'i' in topfivestring:
	    score += 1

	return score
'''
def calc_str_score(s):
	s = s.lower()
	letters = collections.Counter(s)
	most_common = letters.most_common()
	# Remove spaces from char freq calculations
	most_common = [i for i in most_common if i[0] != ' ']
	mc_array = []
	for k,v in most_common:
	    if k != ' ':
	        k = k.lower()
	        mc_array.append(k)
		#print mc_array
	topfivestring = str(mc_array[0]+mc_array[1]+mc_array[2]+mc_array[3]+mc_array[4]+mc_array[5]+mc_array[6]+mc_array[7]+mc_array[8]+mc_array[9]+mc_array[10])

	score = 0

	if 'e' in topfivestring:
	    score += 1
	if 'a' in topfivestring:
	    score += 1
	if 't' in topfivestring:
	    score += 1
	if 'o' in topfivestring:
	    score += 1
	if 'n' in topfivestring:
	    score += 1
	if 'i' in topfivestring:
	    score += 1

	etaoinpass = False
	if score >= 4:
		etaoinpass = True

	if etaoinpass == True:
		if topfivestring[0] == 'e':
			score += 2
		if topfivestring[0] == 't' or topfivestring[1] == 't':
			score += 2

	return score

def xor(s1, s2):
	s1 = s1.lower()
	s2 = s2.lower()
	return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2))

def expandkey(key, ct):
	expansion_length = len(ct)
	expanded_key = (key * ((expansion_length/len(key))+1))[:expansion_length]
	return expanded_key

def bruteforce(s2):
	#Preprocess ciphertext
	s2 = s2.rstrip()
	s2 = s2.lower()
	#s2 = s2.decode("hex")

	
	#Initialize key and best scores
	k = ' '
	best_score = 0
	best_pt_attempt = ''
	best_res = []
	best_k = ''
	

	while hex(ord(k)) != '0xFF': 
		#Expand key from single character to length of ciphertext
		exp_key = expandkey(k, s2)

		#Xor
		pt_attempt = xor(exp_key, s2)
		pt_attempt = pt_attempt.lower()

		#Score output
		score = calc_str_score(pt_attempt)

		#Print / store best result
		if score > best_score:
			best_score = score
			best_pt_attempt = pt_attempt
			best_k = k
			#print "Best Plaintext Guess and Score with key: " 
			#print k, pt_attempt, best_score
			#print '\n'
			
		if ord(k) < 255:
			k = chr(ord(k) + 1)
		else:
			break
	best_res = [best_score, best_k]
	return best_res

def hammingDist (s1, s2):
	#assert len(s1) == len(s2)
	s1 = ''.join(format(ord(x), '08b') for x in s1)
	s2 = ''.join(format(ord(x), '08b') for x in s2)

	return sum(c1 != c2 for c1,c2 in zip(s1,s2))

def decryptMultiByteXOR(ct, k):
	exp_k = expandkey(k, ct.lower())
	pt = xor(exp_k, ct.lower())
	return pt

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def findKeySize():
	smallest_mean_nhd = 99999
	best_KEYSIZE = 0
	KEYSIZE = 1
	while KEYSIZE <= 40:
		chunks = list(chunkstring(ct.lower(), KEYSIZE*2))
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

'''
Test
s1 = "this is a test"
s2 = "wokka wokka!!!"

print hammingDist(s1, s2) #should be 37
'''

# Load file, strip newlines, concat strings, b64 decode
with open('6.txt') as f:
	b64str = "".join(line.strip() for line in f)
	ct = base64.b64decode(b64str).lower()

# Grab KEYSIZE*2 characters from ct, find hamming distance between them
# Divide by KEYSIZE to get normalized_hamming_distance (nhd), keep track of smallest and assoc keysize


KEYSIZE = findKeySize()

# best_keysize = 5

# Break ct into blocks of best_keysize lengths
initblockpass = [ct[i:i+KEYSIZE] for i in range(0, len(ct), KEYSIZE)]

# Explode out block to prepare for transpose
explodeblock = []
for block in initblockpass:
	explodeblock.append(list(block))

transposedblocks = map(list, map(None, *explodeblock))
compressedtranspose = []
for block in transposedblocks:
	compressedtranspose.append(''.join(item for item in block if item))

key = []
for block in compressedtranspose:
	#print len(block)
	# Detect single byte XOR using previous code for each block
	# Key that produces best plaintext for each block is single char key for that block
	# Join chars together for full key
	res = bruteforce(block)
	if res[0] >= 4:
		#print res[0], res[1]
		key.append(res[1])

k = ''.join(x for x in key)
#print k

print decryptMultiByteXOR(ct, k)





