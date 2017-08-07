import binascii
import base64
import sys
import argparse

#User input of plaintext here
parser = argparse.ArgumentParser(usage = '%(prog)s -p -k')
parser.add_argument("-p", dest = "p", help="encrypt plaintext with key using multibyte xor")

#User input of key
parser.add_argument("-k", dest = "k", help="encrypt plaintext with key using multibyte xor")

args = parser.parse_args()
p = args.p
k = args.k

def expandkey(key, ct):
	expansion_length = len(ct)
	expanded_key = (key * ((expansion_length/len(key))+1))[:expansion_length]
	return expanded_key

def xor(s1, s2):
	return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2))

exp_k = expandkey(k, p)

print xor(exp_k, p).encode("hex")