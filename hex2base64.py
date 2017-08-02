import binascii
import base64
import sys
import argparse

#User input of hex string here
parser = argparse.ArgumentParser(usage = '%(prog)s hex_string')
parser.add_argument("hex_string", help="convert hex_string to base64")
args = parser.parse_args()
hx = args.hex_string

#Validate string is hex, decode
try:
    decoded_hex = hx.decode('hex')
except TypeError:
    print "Invalid hex input."
    sys.exit(0)

#Encode to base64 and print
b64_string = decoded_hex.encode('base64')
print b64_string.strip()
