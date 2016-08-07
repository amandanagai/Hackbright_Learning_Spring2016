from sys import exit

# shopping_lists = {'target' : [ 'banana', 'apple', 'Computer' ]}

# print shopping_lists

# # is Banana in target list?
# # is computer in target list?
# user_choice = 'Banana'

# for item in shopping_lists["target"]:
# 	if item.lower() == user_choice.lower()

# exit()

def show_all_lists():
	print "Your shopping lists are:"
	for list_name in shopping_lists.keys():
		print list_name

def show_list(key):
	if key not in shopping_lists.keys():
		print "That list doesn't exist. Add it first."
	else:
		print "The contents of", key, "are:"
		shopping_lists[key].sort()
		for item in shopping_lists[key]:
			print item

def add_list(key):
	if key in shopping_lists:
		print "List already exists. Choose another name."
	else:
		shopping_lists[key] = []
	#Just checking if new list was added:
		print "Your shopping lists are:"
		for list_name in shopping_lists.keys():
			print list_name

def add_item_list(key, value):
	if value in shopping_lists[key]:
		print "Item already exists in %s." % key
	else:
		shopping_lists[key].append(value)
		shopping_lists[key].sort()
		print shopping_lists[key]


def remove_list(key):
	confirm = raw_input("Are you sure you want to delete the %s list? Y or N: " % key)
	if confirm.lower() == "n" or confirm.lower() == "no":
		print "OK, back to Main Menu."
	else:
		del shopping_lists[key]

def remove_item_list(key, value):
	nixed = shopping_lists[key].index(value)
	del shopping_lists[key][nixed]
	print shopping_lists[key]


def menu():
	print """Main Menu:
	0 - Show all lists.
	1 - Show a specific list.
	2 - Add a new shopping list.
	3 - Add an item to a shopping list.
	4 - Remove an item from a shopping list.
	5 - Remove a list by nickname.
	6 - Exit when you are done."""

	user_choice = int(raw_input("Type the option number of your choice: "))
	if user_choice == 0:
		show_all_lists()
	elif user_choice == 1:
		list_choice = raw_input("Which list do you want to see? Enter name: ")
		show_list(list_choice)
	elif user_choice == 2:
		mk_list = raw_input("What do you want to call the new list?")
		add_list(mk_list)
	elif user_choice == 3:
		list_to_append = raw_input("What list do you want to add to?")	
		if list_to_append not in shopping_lists.keys():
			print "We don't have that list. Try adding it first."
		else:
			item = raw_input("Great. What do you want to add to %s? " % list_to_append)
			add_item_list(list_to_append, item)

			while True:
				item = raw_input("Anything else for list %s? " % list_to_append)
				if item.lower() == "n" or item.lower() == "no":
					break
				else:
					add_item_list(list_to_append, item)
			
	elif user_choice == 4:
		list_to_rm_from = raw_input("What list do you want to remove from?")
		if list_to_rm_from not in shopping_lists.keys():
			print "We don't have that list. Try adding it first."
		else:
			Xthis = raw_input("Which item do you want to remove from %s?" % list_to_rm_from)
			for item in shopping_lists:
				if item.lower() != Xthis.lower():
					print "It's not on the list."
				else:
					remove_item_list(list_to_rm_from, item)

	elif user_choice == 5:
		rm_list = raw_input("What list do you want to delete?")
		remove_list(rm_list)
	elif user_choice == 6:
		print "Thank you. Bye."
		exit()
	else:
		print "We didn't understand your entry. Try again."



#begin main program
shopping_lists = {}
while True:
	menu()
	print
