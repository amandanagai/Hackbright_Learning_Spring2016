fav_food = "peanut butter"
fav_movie = "Mrs.Doubtfire"
movie_price = 12.99

def friday_decider(price_peanutbutter=4.95):
	friday_activity = 0
	if price_peanutbutter < movie_price:
		friday_activity = fav_food
	else:
		friday_activity = fav_movie
	print "Budgets suck. Friday, it's you and %s" % friday_activity
	return friday_activity
