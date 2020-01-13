# Q]https://cryptopals.com/sets/1/challenges/1
'''
Convert hex to base64

The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
'''

import binascii
hex_data = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'  #we add the prefix '0x' as our data represents hex encoded ascii
ascii_data = binascii.unhexlify(hex_data)                                                                        #converting hex data to ascii
print(ascii_data)                         																		 #Printing value of ascii_data
base64_data = binascii.b2a_base64(ascii_data)                                                                    #converting ascii_data to base64
print(str(base64_data))                                                                                               #Printing base64_data