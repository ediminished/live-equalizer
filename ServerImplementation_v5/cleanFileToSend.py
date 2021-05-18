import pickle
import numpy
def removeOutliers(data):
#	file = open('cleanerfile2send', 'rb')
#	data = pickle.load(file)	
#	file.close()

	temp = []
	arrayOfGenre = []
	for item in range(0,14):
		arrayOfGenre.append(0) 
		
	for item in data:
		print(type(item[0]),type(item[1]))
	count = 0
	print(type(data[0]), type(data[1]))
	print("dcfvgbhnm")
	for item in data:
		temp.append(item[1])

	threshold = 0.5*len(temp)
	
	#Black box
	i = 0
	while i<10: 
		for item in range(len(temp)):
			if item!=0 and item!=(len(temp)-1):
				if temp[item-1]==temp[item+1]:
					temp[item]=temp[item-1]

		for item in range(len(temp)):
			if item!=0 and item!=(len(temp)-1) and (item!=1 and item!=(len(temp)-2)):
				if temp[item-2]==temp[item+2]:
					temp[item]=temp[item-1]	

		i = i+1
	
	for item in range(len(temp)):
		arrayOfGenre[temp[item]] = arrayOfGenre[temp[item]] + 1; 

	for item in range(len(arrayOfGenre)):
		if arrayOfGenre[item] >= threshold:
			for item2 in range(len(temp)):
				temp[item2] = item

	#for item in range(len(arrayOfGenre)):
	#	print(arrayOfGenre[item])


	#for item in range(len(temp)):
	#	print(temp[item])

	for item in range(len(data)):
		data[item][1] = temp[item]

	tempTemp = []
	for item in data:
		tempTemp.append([item[0], numpy.int64(item[1])])

	
	print("dfvgbhnsdhsdgshjd")
	for item in tempTemp:
		print(type(item[0]),type(item[1]))
	
	return tempTemp
	















#	for item in range(len(data)):
#		 #item < ((len(data))-1) and 
#		if item!=0 and item<(len(data)-3):
#			if data[item][1] != data[item+1][1] or  (data[item+1][1] != data[item+2][1] or data[item+2][1] != data[item+3][1]):
#				data[item][1] = data[item -1][1]
#		data[len(data)-1] = data[len(data)-2]
	
#	for item in range(len(data)):
#		print( data[item][1])	
		

def Main():
	removeOutliers()

if __name__ == "__main__":
	Main()