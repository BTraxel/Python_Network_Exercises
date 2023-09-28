import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 55000

BUFFER_SIZE = 1024
discussing = True

while discussing:
    discussing_raw = input("Do you want to send a message?\n0. No\n1. Yes\nEnter 0 or 1: ")

    while discussing_raw not in ['0', '1']:
        print("Invalid input. Please enter 0 or 1.")
        discussing_raw = input("Enter 0 or 1: ")

    discussing = bool(int(discussing_raw))

    http_head = f"POST/contro_eval.html/1.1\r\n"
    http_head += f"HOST: {TCP_IP}:{TCP_PORT}\r\n"

    if discussing:
        Name = input("Name: ")
        msg = input("Message: ")

        Command = input("Choose a command:\n1. Length of the message\n2. Check if all characters are digits\n3. Convert to uppercase\nEnter 1, 2, or 3: ")

        while Command not in ['1', '2', '3']:
            print("Invalid input. Please enter 1, 2, or 3.")
            Command = input("Enter 1, 2, or 3: ")

        if Command == "1":
            length = len(msg)
            http_head += f"Content_Length: {length}\r\n"
            http_head += f"String= {msg} and Command= Length of the message\r\n"
        elif Command == "2":
            is_digit = msg.isdigit()
            http_head += f"Are all characters digits: {is_digit}\r\n"
            http_head += f"String= {msg} and Command= Check if all characters are digits\r\n"
        elif Command == "3":
            upper_msg = msg.upper()
            http_head += f"Upper case characters: {upper_msg}\r\n"
            http_head += f"String= {upper_msg} and Command= Convert to uppercase\r\n"
    
    else:
        http_head += "Terminate program\r\n"

    http_head = http_head.encode("ascii")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    print(f'Connecting to {TCP_IP}:{TCP_PORT}...')
    s.send(http_head)
    print('Sending data...')  
    rawdata = s.recv(BUFFER_SIZE)
    data = rawdata.decode("ascii")
    print(f"Received data back:\n{data}")

print("Closing the socket")
s.close()
