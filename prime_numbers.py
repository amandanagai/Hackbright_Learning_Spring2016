# i = int(raw_input("Enter a number"))

# for i in i > 1:
# 	if i%(i-1) != 0:
# 		i = i - 1 
# 	else:
# 		print "number is not prime"



def is_prime(number):
	res = True
	for i in range(2, number):
		if number % i == 0:
			# return False
			res = False
		
	return res


def main():
	while True:
	 	user_num = raw_input("Enter a number to check if it's prime: ")
 		if user_num.lower() == "exit" or user_num.lower() == "done":
 			break
 		elif is_prime(int(user_num)) == False:
 			print "Your number is not prime."
		else:
		 	print "It's a prime number!"

if __name__ == '__main__':
		main()	