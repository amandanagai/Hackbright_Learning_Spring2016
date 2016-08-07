#Skeleton code

shopping_lists = {}

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
		mk_item = raw_input("Great. What do you want to add to", list_to_append "?")
		add_item_list(list_to_append, mk_item)
	elif user_choice == 4:
		list_to_rm_from = raw_input("What list do you want to remove from?")
		rm_item = raw_input("Which item do you want to remove from", list_to_rm_from "?")
		remove_item_list(list_to_rm_from, rm_item)
	elif user_choice == 5:
		rm_list = raw_input("What list do you want to delete?")
		remove_list(rm_list)
	elif user_choice == 6:
		print "Thank you. Bye."
	else:
		print "We didn't understand your entry. Try again"
		menu()


def show_all_lists():
	print "Your shopping lists are:"
	for list_name in shopping_lists.keys():
		print list_name

def show_list(key):
	print "The contents of", key, "are:"
	for item in shopping_lists[key]:
		print item

def add_list(key):
	if key in shopping_lists:
		print "List already exists. Choose another name."
		menu()
	shopping_lists[key] = []
	#Just checking if new list was added:
	print "Your shopping lists are:"
	for list_name in shopping_lists.keys():
		print list_name

def add_item_list(key, value):
	shopping_lists[key].append(value)

def remove_list(key):
	pass

def remove_item_list(key, value):
	pass

def exit():