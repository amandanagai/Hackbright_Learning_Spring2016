# num = 3

# def summation(num):
# 	# base case
# 	if num <= 0:
# 		return 0

# 	# recursive call + return a value
# 	return num + summation(num - 1)

# print summation(num)



# def sum_num2(num2):
# 	if num2 <= 0:
# 		res2 = num2 + sum_num2(num2 + 1)
# 		return res2
# 		print res2
# 	else: 
# 		print num2, "is not a negative number."


def neg_sum(num):
	# base case
	if num >= 0:
		return 0

	return num + neg_sum(num + 1)

num_list = []

# num = 2
for num in num_list:
	num = raw_input('enter a negative number: ')
	if type(num) != int:
		print "hey, that's not a number!"
	elif num > 0:
		print "hey, I said negative!!"
	else:
		print neg_sum(num)
