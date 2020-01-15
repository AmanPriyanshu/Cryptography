'''
Single-byte XOR cipher

The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score. 
'''
import binascii
import string
def score(text):
	alphabet = string.ascii_lowercase + string.ascii_lowercase.upper() + ' '
	str_score = 0
	for i in text:
		if i in alphabet:
			str_score += 1
	return str_score



def text_XOR_scroing(input_hex):
	list_decrypted = []
	#input_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
	ascii_input = binascii.a2b_hex(input_hex)
	j = 0
	for i in range(256):
		final_output = ''
		for j in ascii_input:
			final_output += chr(ord(j)^i)
		list_decrypted.append({'decrypted text' : final_output, 'score' : score(final_output)})

	maximum = 0
	maximum_score = list_decrypted[0]['score']
	for i in range(1, len(list_decrypted)):
		if list_decrypted[i]['score'] > maximum_score:
			maximum = i
			maximum_score = list_decrypted[i]['score']
	return list_decrypted

#print()