
#create a list
#add to a list
	#check for duplication
	#reject duplicates with messages
#print list

shopping_list = []

def listing(item):
	if item.lower() in shopping_list:
		print "List already contains", item
	else:
		shopping_list.append(item)
		shopping_list.sort()
		print shopping_list	
		return shopping_list
		

while True:
	input_item = raw_input("What do you want to add to the list? ").lower()

	if input_item == "remove item" or input_item == "remove" or input_item == "delete":
		removed_item = raw_input("What item do you want to remove?").lower()
		if removed_item not in shopping_list:
			print "Item not in list"
		else:
			shopping_list.remove(removed_item)
			print shopping_list

	elif not input_item or input_item.lower() == "done":
		break

	else:
		listing(input_item)
