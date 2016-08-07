from codeappetizer_june14 import *
import requests


response = requests.get("https://data.sfgov.org/resource/wwmu-gmzc.json")

movie_list = []
movie_titles = [movie.title for movie in response.json()]
# movie_list = []

# for movie in response.json():
# 	# mov = Movie_info(
# 	# 	movie['director'],
# 	# 	movie['release_year'],
# 	# 	movie['title'],
# 	# 	movie.get('actor_1', None),
# 	# 	movie.get('locations', None),
# 	# 	movie.get('actor_2', None)
# 	# )

# 	# movie_list.append(mov)
# 	# print mov

# 	mov = Movie_info(**movie)
# 	if mov.title not in movie_titles:
# 		movie_titles.append(mov.title)
# 		movie_list.append(mov)

# # for movie in movie_titles:
# # 	print movie

# for movie in movie_list:
# 	print movie