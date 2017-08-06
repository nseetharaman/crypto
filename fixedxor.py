# XOR two hex strings

str1 = "1c0111001f010100061a024b53535009181c"
str2 = "686974207468652062756c6c277320657965"

str1 = str1.decode("hex")
str2 = str2.decode("hex")

'''
def xor(s1, s2):
    strxor = format(int(s1, 16) ^ int(s2, 16), 'x')
    return strxor
'''


def xor(s1, s2):
	return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2))

result = xor(str1, str2).encode("hex")

print(result)
