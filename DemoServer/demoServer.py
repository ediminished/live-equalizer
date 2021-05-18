import socket
port = 55555

def Main():
	s = socket.socket()
	print ("socket created... ✅")
	s.bind (('',port))
	print ("socket binded to", port, "  ✅")
	s.listen(5)
	while True:
		c, addr = s.accept()
		print ("Got connection from ", addr)
		f = open ("file2send", "rb")
		l = f.read(1024)
		while(l):
			print("Sending...")
			c.send(l)
			l = f.read(1024)
		f.close()
		s.shutdown(socket.SHUT_WR)
	print("Send.!!")

if __name__ == "__main__":
	Main()