import socket
from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("chatapplication.key", "wb") as key_file:
    key_file.write(key)

cipher_suite = Fernet(key)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(5)

print("Server is listening...")

client_socket, client_address = server_socket.accept()

while True:
    
    encrypted_message = client_socket.recv(1024)
    
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    
    print(f"Client: {decrypted_message.decode()}")

    message = input("You: ")
    encrypted_message = cipher_suite.encrypt(message.encode())
    client_socket.send(encrypted_message)
