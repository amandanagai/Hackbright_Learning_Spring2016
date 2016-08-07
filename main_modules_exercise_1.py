import lib_modules_exercise_1   #or "from lib_modules_exercise_1 import *"
from lib_modules_exercise_1 import friday_decider

#inflation has struck
price = float(raw_input("What is the price of peanut butter today?"))

friday_decider(price)