from contacts import *

contact_list = []


def add_contact(first, last, tweet_handle="",email_address="", address="", birthday=""):
	new_contact = Contact(first, last, tweet_handle, email_address, address, birthday)
	contact_list.append(new_contact) 

def remove_contact(first, last, tweet_handle="",email_address="", address="", birthday=""):
	i = 0
	while i < len(contact_list):
		if contact_list[i].last_name == "pepper":
			del contact_list[i]
		i += 1

			# if len(contact_list[i].email_address) > 0:
			# 	contact_list[i].email_address = ""

def change_contact():
	chosen_contact = raw_input("Enter the last name of contact you want to edit:")
	choice = raw_input("What do you want to change?\n1-firstname\n2-lastname\n3-twitterhandle\n4-email address\n5-address\n6-birthday\n")
	new_value = raw_input("Type the new value:")
	i = 0
	while i < len(contact_list):
		if contact_list[i].last_name == chosen_contact and choice == "1":
			contact_list[i].first_name = new_value
		elif contact_list[i].last_name == chosen_contact and choice == "2":
			contact_list[i].last_name = new_value
		elif contact_list[i].last_name == chosen_contact and choice == "3":
			contact_list[i].tweet_handle = new_value
		elif contact_list[i].last_name == chosen_contact and choice == "4":
			contact_list[i].email_address = new_value
		elif contact_list[i].last_name == chosen_contact and choice == "5":
			contact_list[i].address = new_value
		elif contact_list[i].last_name == chosen_contact and choice == "4":
			contact_list[i].birthday = new_value
		i += 1

def show_contact():
	chosen_contact = raw_input("Enter the last name of contact you want to view:")
	for person in contact_list:
		if person.last_name == chosen_contact:
			print person.first_name, person.last_name, person.tweet_handle, person.email_address, person.address, person.birthday
			# print person.__dict__

def show_sorted_list():
	pass

add_contact("danielle", "pepper")
add_contact("amy", "brant", email_address="bee@gmail.com")
for person in contact_list:
	print person.last_name, person.first_name, person.email_address

show_contact()
# change_contact()
# remove_contact("danielle", "pepper")

# for person in contact_list:
# 	print person.last_name, person.first_name, person.email_address