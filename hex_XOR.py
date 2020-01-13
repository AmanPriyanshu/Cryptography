'''
Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965

... should produce:

746865206b696420646f6e277420706c6179
'''
import binascii
input_hex = '1c0111001f010100061a024b53535009181c'         
binary_input = binascii.a2b_hex(input_hex)                     #converting hex to ascii
key_hex = '686974207468652062756c6c277320657965'
binary_key = binascii.a2b_hex(key_hex)                         #converting hex to ascii
final_data = ''
for i,j in zip(binary_key, binary_input):
	final_data += chr(i^j)                                     #XORing the 2
print(final_data)                                              #printing final_data