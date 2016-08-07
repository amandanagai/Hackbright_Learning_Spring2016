
def decode():
	code = raw_input("What is the code?")

	nums = []
	for n in range(0,10):
		nums.append(str(n))
	
	codeword_letters = []
	for letter in code:
		codeword_letters.append(letter)

	rectified_list = []
	for letter in codeword_letters:
		if letter in nums:
			rectified_list.append(int(letter))
		else:
			rectified_list.append(letter)

	decoded_list = []
	for letter in rectified_list:
		if type(letter) == int:
			index = rectified_list.index(letter)
			decoded_list.append(rectified_list[index+letter+1])

	message = "%s" % (''.join(decoded_list))

	print message
	return message


def main():
	decode()

if __name__ == '__main__':
	main()