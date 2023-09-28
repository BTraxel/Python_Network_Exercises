import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 55000
BUFFER_SIZE = 1024

sconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sconn.bind((TCP_IP, TCP_PORT))
print(f"Binding to {TCP_IP}:{TCP_PORT} ...")
sconn.listen(1)

while True:
    print("Waiting for a client ...")
    s, addr = sconn.accept()
    print(f'Client connected with address: {addr}')
    rawdata = s.recv(BUFFER_SIZE)
    print("Received data:", rawdata)
    # Split the received message by '\r\n' and print each line separately
    msg_lines = rawdata.decode('ascii').split('\r\n')
    print("Decrypted message: ")
    msg = ''
    for line in msg_lines:
        print(line)
        msg += line
    
    http_head = "HTTP/1.1 200 OK\r\n"
    http_head += f"HOST: {TCP_IP}:{TCP_PORT}\r\n"
    http_head += "Content-Type: text/plain\r\n"
    http_head += f"Content-length: {len(msg)}\r\n"
    
    print(f"Sending back processed answer:\n{http_head}")
    
    http_head = http_head.encode("ascii")

   
    s.send(http_head)

    if "Terminate program" in msg:
        print("Received termination command. Closing the server.")
        s.close()
        sconn.close()
        break
