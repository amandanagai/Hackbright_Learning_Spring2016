my_name = "Erika"
print list(my_name)

print "1,2,3,4,5".split(',')

#re_fish_list = "One fish two fish red fish blue fish".split(" fish ")

re_fish_list = "One fish two fish red fish blue fish".replace(" fish", "").split(" ")
#re_fish_list.replace(" fish", "")
print re_fish_list

grocery_list = "item:apples,quantity:4,price:1.50\n".strip().split(",")
grocery_bill = float(grocery_list[1].split(":")[1]) * float(grocery_list[2].split(":")[1])
print grocery_bill

# grocery_list = "item:apples,quantity:4,price:1.50\n".strip().strip("item:apples,").split(",")
# # grocery_bill = float(grocery_list[1].split(":")[1]) * float(grocery_list[2].split(":")[1])
# grocery_re_list = grocery_list.split(":")
# grocery_bill = float(grocery_re_list[1]) * float(grocery_re_list[3])
# print grocery_bill
def make_variable_str(num, string):
	return string[num].strip().split(",")

def total_subitem_price(variable):
	return float(variable[1].split(":")[1]) * float(variable[2].split(":")[1])

items = ["item:apples,quantity:4,price:1.50\n", "item:pears,quantity:5,price:2.00\n", "item:cereal,quantity:1,price:4.49\n"]
apples = make_variable_str(0, items)  #items[0].strip().split(",") 
pears = make_variable_str(1, items)  #items[1].strip().split(",")
cereal = make_variable_str(2, items) #items[2].strip().split(",")

total_bill = total_subitem_price(apples) + total_subitem_price(pears) + total_subitem_price(cereal)
print total_bill