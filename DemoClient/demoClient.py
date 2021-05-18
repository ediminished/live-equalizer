import socket
import pickle

# desiredSize = 128
# port = 55555


# print ("Connecting...")

# s=socket.socket()
# s.connect(('127.0.0.1', port))


# print ("connected to server...")


# f = open('file2send','wb') # Open in binary
# l = s.recv(1024)
# while (l):
# 	print ("Receiving...")
# 	f.write(l)
# 	l = s.recv(1024)
# f.close()
# print (s.recv(1024))
# s.close()
# print ("Recieved....")
pickle_in = open("file2send","rb")
genre_dict = pickle.load(pickle_in)
print (genre_dict)