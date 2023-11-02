import socket
from cryptography.fernet import Fernet

with open("server_key.key", "rb") as key_file:
    server_key = key_file.read()
key = server_key
cipher_suite = Fernet(key)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(1)

print("Server is listening...")

while True:
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")
    
    with conn:
        data = conn.recv(1024)
        decrypted_data = cipher_suite.decrypt(data)
        with open("backup.dat", "wb") as file:
            file.write(decrypted_data)
            print("Data received and stored securely.")
