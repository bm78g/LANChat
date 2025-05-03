import socket
import threading

# Server accepts any incoming IP and uses port 12345
HOST = '0.0.0.0'
PORT = 12345

# Binds server to IP and port and begins listening
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

# Adds newcoming clients and broadcasts any received messages
# Removes terminated clients
def handle_client(conn, addr):
    print(f"{addr} has connected.")
    while True:
        try:
            message = conn.recv(1024)
            print(f"Message sent from {addr}:\n{message}")
            broadcast(message, conn)
        except:
            print(f"Connection from {addr} terminated")
            clients.remove(conn)
            conn.close()
            break

# Sends message to every socket except for the sender's
def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            client.send(message)
        
print("Server is running.")

# Begins a new thread for any new connections
while True:
    conn, addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn, addr)).start()