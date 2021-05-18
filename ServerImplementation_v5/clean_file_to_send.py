import pickle
file = open('file2send', 'rb')

data = pickle.load(file)

file.close()

for item in data:
	print(item[0], item[1])