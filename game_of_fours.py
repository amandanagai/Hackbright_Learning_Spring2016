zero_string = "44-44"
print "%s = %i" % (zero_string, eval(zero_string))

one_string = "44/44"
print "%s = %i" % (one_string, eval(one_string))

two_string = "(44/4)/4"
print "%s = %i" % (two_string, eval(two_string))

three_string = "(4+4+4)/4"
print "%s = %i" % (three_string, eval(three_string))

four_string = "((4/4)+(4/4))**2"
print "%s = %i" % (four_string, eval(four_string))

five_string = "((4*4)+4)/4"
print "%s = %i" % (five_string, eval(five_string))

six_string = "((4+4)/4)+4"
print "%s = %i" % (six_string, eval(six_string))

seven_string = "(4+4)-(4/4)"
print "%s = %i" % (seven_string, eval(seven_string))

eight_string = "(4+4)+(4-4)"
print "%s = %i" % (eight_string, eval(eight_string))

nine_string = "(4+4)+(4/4)"
print "%s = %i" % (nine_string, eval(nine_string))

ten_string = "(44-4)/4"
print "%s = %i" % (ten_string, eval(ten_string))