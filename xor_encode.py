#!/usr/bin/python


#example originalshellcode="\x01\xAB"
originalshellcode=""

encodeshellcode=""

# XOR Encoding
for i in bytearray(originalshellcode):

    j=i ^ 0x12
    encodeshellcode += '\\x'
    encodeshellcode += '%02x' % j

print encodeshellcode
print encodeshellcode.replace(r"\x"," ")