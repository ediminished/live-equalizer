#!/usr/bin/env python  
  
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer  
import os  
  
#Create custom HTTPRequestHandler class  
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):  

  #handle GET command  
  def do_GET(self):
    try:  
      

        

    except IOError:  
      self.send_error(404, 'file not found')  

def run():  
  print('http server is starting...')  
  
  #ip and port of servr  
  #by default http server port is 80  
  server_address = ('127.0.0.1', 80)  
  httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)  
  print('http server is running...')  
  httpd.serve_forever()  

if __name__ == '__main__':  
  run()  