import socket

port = 5060
data = 16
format = "utf-8"
disconnected_msg = "Done"
hostname = socket.gethostname()
host_addr = socket.gethostbyname(hostname)

server_socket_address = (host_addr, port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_address)

def msg_send(msg):
    message = msg.encode(format)
    msg_length = len(message)
    msg_length = str(msg_length).encode(format)
    msg_length += b" " * (data - len(msg_length))

    client.send(msg_length)
    client.send(message)

    response = client.recv(2048).decode(format)
    print(response)
    return response

while True:
    input_msg = input("Enter work hours or type 'Done' to disconnect: ")
    response = msg_send(input_msg)
    if input_msg == disconnected_msg:
        print("Disconnecting from the server...")
        break

client.close()
