
file = open('./photos/test.jpeg', mode='rb')
for chunk in file.read():
	print(chunk)

