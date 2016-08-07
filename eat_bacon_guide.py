"""Questions your bacon eating interest, guides you through a tree, and every answer tries to get you to eat it"""


def main():
	answer = raw_input("Do you want to feel like angels are frockling on your taste buds?")
	if answer.upper() == "YES!":
		print "Eat it"
	elif answer == "Yes":
		answer2 = raw_input("Are you a coward?")
		if answer2 == "I am not!" or answer2 == "No":
			print "Then eat it"
		else:
			print "Bacon will turn you into a true warrior"
	else:
		print "You've clearly never tasted bacon"
		print "Eat it"


if __name__ == '__main__':
	main()