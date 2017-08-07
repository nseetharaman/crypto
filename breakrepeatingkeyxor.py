import base64

def hammingDist (s1, s2):
	#assert len(s1) == len(s2)
	s1 = ''.join(format(ord(x), '08b') for x in s1)
	s2 = ''.join(format(ord(x), '08b') for x in s2)

	return sum(c1 != c2 for c1,c2 in zip(s1,s2))

s1 = "this is a test"
s2 = "wokka wokka!!!"



s3 = "HUIfTQsPAh9PE048GmllH0kcDk4TAQsHThsBFkU2AB4BSWQgVB0dQzNTTmVS"
s4 = "BgBHVBwNRU0HBAxTEjwMHghJGgkRTxRMIRpHKwAFHUdZEQQJAGQmB1MANxYG"

print hammingDist(s3, s4)