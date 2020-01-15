from hex_XOR_unit_key import score, text_XOR_scroing

file1 = open("hex_XOR_data.txt","r")
data_list = file1.readlines()
list_decrypted = []
for i in data_list:
	#print(i[:-1])
	list_decrypted += text_XOR_scroing(i[:-1])
	#print(text_XOR_scroing(i[:-1]))

print(len(list_decrypted))

maximum = 0
maximum_score = list_decrypted[0]['score']
for i in range(1, len(list_decrypted)):
	if list_decrypted[i]['score'] > maximum_score:
		maximum = i
		maximum_score = list_decrypted[i]['score']
print(list_decrypted[maximum])