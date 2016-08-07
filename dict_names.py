
"""function that counts number of times each letter appears in your name"""
#get name as raw input
#check first letter in rest of string-count letters and return as dic entry
#if entry already exists, skip
#iterate to the end of string
#return dic




def count_my_name(name):
	name_dic = {}
	for letter in name.lower():
		if letter not in name_dic:
			name_dic[letter] = 1
		elif letter in name_dic:
			name_dic[letter] += 1
	return name_dic

def main():
	my_name = raw_input("What is your full name?").lower()
	print count_my_name(my_name)
	return count_my_name(my_name)

if __name__ == '__main__':
	main()