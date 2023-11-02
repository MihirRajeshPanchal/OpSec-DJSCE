import socket

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    auth_status = input("Enter 'auth' for authenticated or 'unauth' for unauthenticated: ")
    client_socket.send(auth_status.encode())

    response = client_socket.recv(1024).decode()
    print(response)

    while True:
        action = input("Enter 'encrypt', 'decrypt', or 'quit': ")
        client_socket.send(action.encode())
        if action == "quit":
            break
        filename = input("Enter the filename: ")
        client_socket.send(filename.encode())
        response = client_socket.recv(1024).decode()
        print(response)

if __name__ == "__main__":
    client()
