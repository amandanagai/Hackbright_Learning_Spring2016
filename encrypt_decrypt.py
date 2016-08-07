# full_name = ('Amanda', 'Nagai')
# full_name_list = list(full_name)
# full_name_list.sort(reverse=True)
# print full_name_list


# for i in range(1000,0,-100):
# 	print i

#sudo En/decrypt Program:

#dictionary - encryption key 
#message
#encrypted message

#function: encryption
#function: decrypt
#function test results
import string

message = "Amanda" #raw_input("What do you want to send encrypted?")   #string


encrypt_dictionary = {}
decrypt_dictionary = {}


def encrypt(message):

	encrypted_msg = ""

	for c in message:
		if c in encrypt_dictionary:
			encrypted_msg += (str(encrypt_dictionary[c]) + "-")
	return encrypted_msg

def decrypt(encrypt_msg):
	decrypt_final = ""

	decrypt_msg = encrypted_msg.split("-")
	decrypt_msg.pop()

	for c in decrypt_msg:
		if int(c) in decrypt_dictionary:
			decrypt_final += decrypt_dictionary[int(c)]
	return decrypt_final

def create_encrypt_decrypt_codes():
	i = 0
	for char in string.printable:
		encrypt_dictionary[char] = i
		decrypt_dictionary[i] = char	
		i += 1

create_encrypt_decrypt_codes()
encrypted_msg = encrypt(message)
print decrypt(encrypted_msg)
# print encrypt_dictionary
# print decrypt_dictionary
# print encrypt(message)