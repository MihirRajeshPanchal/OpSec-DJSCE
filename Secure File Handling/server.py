import socket
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open('key.key', 'rb').read()

def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server is listening...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")

        request = client_socket.recv(1024).decode()
        if request == "auth":
            key = load_key()
            client_socket.send("Authenticated".encode())
        else:
            key = None
            client_socket.send("Unauthenticated".encode())

        while True:
            action = client_socket.recv(1024).decode()
            if action == "encrypt":
                filename = client_socket.recv(1024).decode()
                encrypt_file(filename, key)
                client_socket.send(f"{filename} encrypted".encode())
            elif action == "decrypt":
                filename = client_socket.recv(1024).decode()
                decrypt_file(filename, key)
                client_socket.send(f"{filename} decrypted".encode())
            elif action == "quit":
                client_socket.close()
                break

if __name__ == "__main__":
    generate_key()
    server()
