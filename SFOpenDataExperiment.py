import requests

resp = requests.get('https://data.sfgov.org/resource/ri9p-p4mm.json')

if resp.status_code != 200:
	print 'Something went wrong.'
for event in resp.json():
	print event["address"]
	# if '*Haight*' in address:
	# 	print address


