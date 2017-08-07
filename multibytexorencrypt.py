'''
Encrypt following string:
Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal

with key 'ICE'
'''

def expandkey(key, ct):
	expansion_length = len(ct)
	expanded_key = (key * ((expansion_length/len(key))+1))[:expansion_length]
	return expanded_key

def xor(s1, s2):
	return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2))

s = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
k = 'ICE'
exp_k = expandkey(k, s)

print xor(exp_k, s).encode("hex")