#This script wont produce anything, it was used to listen to data sent from a sensor

import socket
import time
import struct
import datetime
import select
format = 'diiiiffff'
a = 1


TCP_IP = '127.0.0.1'
TCP_PORT = 55000
BUFFER_SIZE = 1024
UDP_IP = '192.168.0.106' #Enter your local IP
UDP_PORT1 = 52001
UDP_PORT2 = 52002
sock1 = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock2 = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
socketList = [sock1,sock2]

sock1.bind((UDP_IP, UDP_PORT1))
sock2.bind((UDP_IP, UDP_PORT2))

sconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sconn.bind((TCP_IP, TCP_PORT))
print("Binding to "+ TCP_IP +":"+str(TCP_PORT)," ...")
sconn.listen(1)

while True:
    ls = select.select(socketList,[],[],1)
    for s in ls[0]:
        data, addr = s.recvfrom(1024) # buffer size is 1024 bytes  
       
        if(s.getsockname()[1] ==  52001):
            print("---------------------------")
            print("Received message", data.decode('ascii'))
            message_to_display = ("Received message : "+str(data.decode('ascii')))
            a = 1
            print("#Message from:",addr)
            print("#Message to :",s.getsockname())
            print("---------------------------")
        elif(a == 1 and s.getsockname()[1] ==  52002):
            print("---------------------------")
            print("Received message", struct.unpack(format,data))
            print(datetime.datetime.fromtimestamp(struct.unpack(format,data)[0]))
            message_to_display = ("Received message, date : "+str(datetime.datetime.fromtimestamp(struct.unpack(format,data)[0]))+" pitch : "+str(struct.unpack(format,data)[1])+" roll : "+str(struct.unpack(format,data)[2])+" yaw : "+str(struct.unpack(format,data)[3])+" battery : "+str(struct.unpack(format,data)[4])+" barometer : "+str(struct.unpack(format,data)[5])+" agx : "+str(struct.unpack(format,data)[6])+" agy : "+str(struct.unpack(format,data)[7])+" agz : "+str(struct.unpack(format,data)[8]))       
            a = 0
            print("#Message from:",addr)
            print("#Message to :",s.getsockname())
            print("---------------------------")
            
            
        http_head = "HTTP/1.1 200 OK\r\n"
        http_head += "Date:"+ time.asctime() +"GMT\r\n"
        http_head += "Expires: -1\r\n"
        http_head += "Cache-Control: private, max-age=0\r\n"
        http_head += "Content-Type: text/html;"
        http_head += "charset=utf-8\r\n"
        http_head += "\r\n"
        data = "<html><head><meta charset='utf-8'/></head>"
        data += "<body><h1>"+message_to_display+"</h1>"
        data += "</body></html>\r\n"
        data += "\r\n"
        http_response = http_head.encode("ascii") + data.encode("utf-8")
        s, addr = sconn.accept()
        print('Client connected with address:', addr)
        rawdata = s.recv(BUFFER_SIZE)
        print("Received data:", rawdata.decode('ascii'))
        s.send(http_response)  









