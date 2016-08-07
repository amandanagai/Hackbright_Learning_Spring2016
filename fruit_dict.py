fruit_dict = {'banana': 4, 'apple':2, 'orange':1.5, "pear": 3}

def most_expensive_item():
	global fruit_dict
	price_list = fruit_dict.values() 
	price_list.sort()
	return price_list[-1]
	
def main():
	most_expensive = most_expensive_item()
	
	for key, value in fruit_dict.items():
		if value == most_expensive:
			print key
			return key


if __name__ == '__main__':
	main()

	# iterating through the dic and variable of highest seen so far and then comparison and overwriting if come across a new one