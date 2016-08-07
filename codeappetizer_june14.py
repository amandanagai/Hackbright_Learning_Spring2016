class Movie_info(object):
	def __init__(self,director,release_year,title,actor_1='',locations='',actor_2='', **kwargs):
		self.director =  director
		self.release_year = release_year
		self.title = title
		self.actor_1 = actor_1
		self.actor_2 = actor_2
		self.locations = locations

	def __str__(self):
		return self.title #+ " " + self.release_year