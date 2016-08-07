import audioop

with open('Combined.mp3', 'w+') as fh:
	fh.write(audioop.add('hello.wav', 'lalala.wav', 1))

