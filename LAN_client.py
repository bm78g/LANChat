import socket
import threading

# TODO: Allow users to transfer files and exit program organically

HOST = '0.0.0.0' #Change to server's address
PORT = 12345

# Connects client to server address
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Listens for message reception
def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("[Error] Connection lost.")
            client.close()
            break

# Listens for client message
def send():
    while True:
        message = input()
        client.send(message.encode())

threading.Thread(target=receive).start()
threading.Thread(target=send).start()