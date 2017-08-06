import collections
import binascii

# Input string

s2 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
s2 = s2.lower()
s2 = s2.decode("hex")

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

	topfivestring = str(mc_array[0]+mc_array[1]+mc_array[2]+mc_array[3]+mc_array[4])

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

	return score


def xor(s1, s2):
	return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2))

def expandkey(key, ct):
	expansion_length = len(ct)
	expanded_key = (key * ((expansion_length/len(key))+1))[:expansion_length]
	return expanded_key

def num2bytes(num):
	res = str(unichr(num))
	return res

#Initialize key guess and score
k = ' '
best_score = 0
print '\n'

#Brute force loop
while hex(ord(k)) != '0xFF': 
	#Expand key from single character to length of ciphertext
	exp_key = expandkey(k, s2)

	#Xor
	pt_attempt = xor(exp_key, s2)

	#Score output
	score = calc_str_score(pt_attempt)

	#Print best result
	if score > best_score:
		best_score = score
		print "Best Plaintext Guess and Score with key: " 
		print k, pt_attempt, best_score
		print '\n'
		
	if ord(k) < 255:
		k = chr(ord(k) + 1)
	else:
		break
