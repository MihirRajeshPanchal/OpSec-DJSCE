import socket
from cryptography.fernet import Fernet

with open("chatapplication.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))

while True:
    
    message = input("You: ")
    encrypted_message = cipher_suite.encrypt(message.encode())
    client_socket.send(encrypted_message)
    
    encrypted_message = client_socket.recv(1024)
    
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    print(f"Server: {decrypted_message.decode()}")
