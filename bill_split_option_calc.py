def bill_total(bill, tip):
	total = bill + (bill*(tip/100))
	return total

def bill_splitting(total, num_people):
	split_amount = total / num_people
	return split_amount

def main():
	print "Welcome to the calc."
	print "You have two options:"
	option = int(raw_input("Enter "1" to calcuate tip, or "2" to split the bill"))
	bill = float(raw_input("What is the bill amount?"))
	tip_percent = float(raw_input("What percent tip do you want to leave (enter without percent sign)?"))
	if option == "1":	
		t_amount = bill_total(bill, tip_percent)
		return t_amount
		print "With tip, the total bill is", t_amount
		next_option = raw_input("Do you want to split the bill?")
		if next_option.upper() == "YES":
			num_people = int(raw_input("How many people shared the meal (in numbers)?"))
			s_amount = bill_splitting(t_amount, num_people)
			return s_amount
			print s_amount
		else:
			break

	if option == "2":
		bill = float(raw_input("What is the bill amount?"))
		tip_percent = float(raw_input("What percent tip do you want to leave (enter without percent sign)?"))
		num_people = int(raw_input("How many people shared the meal (in numbers)?"))
		t_amount = bill_total(bill, tip_percent)
		s_amount = bill_splitting(t_amount, num_people)
		print s_amount