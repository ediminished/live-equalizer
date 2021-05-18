
#import http.client

##connection.request("GET", "/")
#response = connection.getresponse()
#print("Status: {} and reason: {}".format(response.status, response.reason))

#connection.close()


import socket
import pickle
import numpy as np
import sys
import os
import time
import numpy as np
import json, codecs
from subprocess import Popen, PIPE, STDOUT
from PIL import Image
# from jsonsocket import Client

from imageFilesTools import getImageData
from audioFilesTools import isMono
from config import batchSize
from config import filesPerGenre
from config import nbEpoch
from config import validationRatio, testRatio
from config import sliceSize
from config import slicesPath
from config import preTemp
from config import pixelPerSecond
from eq_changer_v5 import changer
from _thread import *
import threading
import http.client
import json
desiredSize = 128
mypath = "Testing\\"
nameIs = "aaa.mp3"
newNameIs = "newa"
conn = http.client.HTTPSConnection('www.httpbin.org')

headers = {'Content-type': 'application/json'}

print ("Starting Client...")
currentPath = os.path.dirname(os.path.realpath(__file__)) 

command = 'sox "{}" "{}.mp3" remix 1,2'.format(nameIs,newNameIs)
p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=False, cwd=currentPath)


output, errors = p.communicate()
if errors:
	print (errors)

command = 'sox "{}.mp3" -n spectrogram -Y 200 -X {} -m -r -o "{}.png"'.format(newNameIs,pixelPerSecond,newNameIs)
p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=False, cwd=currentPath)
output, errors = p.communicate()
if errors:
	print (errors)

img = Image.open(newNameIs+".png")

img.save("akimage.png")

#Compute approximate number of 128x128 samples
width, height = img.size
nbSamples = int(width/desiredSize)
width - desiredSize

#For each sample
#for i in range(nbSamples):
	#Extract and save 128x128 sample
#	startPixel = i*desiredSize
#	imgTmp = img.crop((startPixel, 1, startPixel + desiredSize, desiredSize + 1))
#	imgTmp.save(mypath+"{}/{}_{}.png".format("",newNameIs[:-4],i))
#	print ("Slices Created... ")		# Create Array
nbClasses = 13
fileNames = os.listdir(mypath)
data = []
trainNb = 0
for i in fileNames:
	imgData = getImageData(mypath+"/"+i, sliceSize)
	data.append((imgData))
	trainNb = trainNb + 1
print ("FEED_DATA #############################################################")
feedData = np.array(data[:trainNb]).reshape([-1, sliceSize, sliceSize, 1])
print(feedData)
datatosend = feedData.tolist()

print ("data_arr created ..........")




#foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
json_data = json.dumps(datatosend)
print('askl')
conn.request('POST', '/post', json_data, headers)
print("sent")
response = conn.getresponse()
print(response.read().decode())
