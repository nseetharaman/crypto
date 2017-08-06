# Encrypt an input string by XORing with single byte key

import binascii

s = "This is my input string. There are many string like it but this one is mine."
k = 'a'

def xor(s1, s2):
	return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2))

def expandkey(key, ct):
	expansion_length = len(ct)
	expanded_key = (key * ((expansion_length/len(key))+1))[:expansion_length]
	return expanded_key

ek = expandkey(k, s)
res = xor(s, ek).encode("hex")

print res