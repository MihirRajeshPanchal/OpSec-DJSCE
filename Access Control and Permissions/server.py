import socket
import os

users = {
    "admin": {"read": True, "write": True, "delete": True},
    "mihir": {"read": True, "write": True, "delete": False},
    "dishant": {"read": True, "write": False, "delete": False},
}

files = {
    "file1.txt": ["admin", "mihir"],
    "file2.txt": ["admin", "dishant"],
}

def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    user, action, filename = request.split()
    
    if user in users and filename in files and users[user][action]:
        if action == "read":
            with open(filename, "rb") as file:
                client_socket.send(file.read())
        elif action == "write":
            data = client_socket.recv(1024)
            with open(filename, "wb") as file:
                file.write(data)
        elif action == "delete":
            os.remove(filename)
            client_socket.send("File deleted".encode())
    else:
        client_socket.send("Access denied".encode())
    
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))
server.listen(5)

print("Server listening on port 12345")

while True:
    client_socket, addr = server.accept()
    print(f"Accepted connection from {addr}")
    handle_client(client_socket)
