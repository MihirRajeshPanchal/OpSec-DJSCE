import socket
from cryptography.fernet import Fernet

with open("server_key.key", "rb") as key_file:
    server_key = key_file.read()
cipher_suite = Fernet(server_key)

with open("data_to_backup.dat", "rb") as file:
    data = file.read()

encrypted_data = cipher_suite.encrypt(data)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))

client_socket.send(encrypted_data)

print("Data sent to the server.")

client_socket.close()
