import socket


UDP_IP = "127.0.0.1"
UDP_PORT = 50005

sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP


sock.bind((UDP_IP, UDP_PORT))

Name = input("Name : ")
FamilyName = input("Family Name : ")

msg=Name+" "+FamilyName
msg = msg.encode("utf8")

sock.sendto(msg,(UDP_IP, UDP_PORT))
print("----------")
data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
print("Received message: ", data.decode('utf8'))
print("From: ",addr)
print("----------")
sock.sendto(data.decode('utf8').encode('utf8'),(UDP_IP, UDP_PORT))
data, addr = sock.recvfrom(1024)
print("Echo")
print("Received message: ", data.decode('utf8'))
print("From: ",addr)
print("----------")
sock.close()





   





