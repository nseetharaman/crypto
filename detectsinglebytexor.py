# Take an input file composed of 60 character strings and find the string that has been encrypted by single char XOR
import collections
import binascii

def calc_str_score(s):
	# Count total letter in input string
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

def xor(s1, s2):
	return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2))

def expandkey(key, ct):
	expansion_length = len(ct)
	expanded_key = (key * ((expansion_length/len(key))+1))[:expansion_length]
	return expanded_key

def bruteforce(s2):
	#Preprocess ciphertext
	s2 = s2.rstrip()
	s2 = s2.decode("hex")
	
	#Initialize key and best scores
	k = ' '
	best_score = 0
	best_pt_attempt = ''
	best_res = []
	

	while hex(ord(k)) != '0xFF': 
		#Expand key from single character to length of ciphertext
		exp_key = expandkey(k, s2)

		#Xor
		pt_attempt = xor(exp_key, s2)

		#Score output
		score = calc_str_score(pt_attempt)

		#Print / store best result
		if score > best_score:
			best_score = score
			best_pt_attempt = pt_attempt
			#print "Best Plaintext Guess and Score with key: " 
			#print k, pt_attempt, best_score
			#print '\n'
			
		if ord(k) < 255:
			k = chr(ord(k) + 1)
		else:
			break
	best_res = [best_score, best_pt_attempt]
	return best_res

# Open input file for processing
f = open('4.txt', 'r')

# Iterate through each line and decrypt + score, print outputs with best score
num = 0

for line in f:
	num += 1
	res = bruteforce(line)
	if res[0] > 3:
		print res, "Line: ", num






