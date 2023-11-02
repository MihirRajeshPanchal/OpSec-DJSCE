import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))

user = "mihir"
action = "read"
filename = "file1.txt"
# user = "dishant"
# action = "write"
# filename = "file2.txt"

request = f"{user} {action} {filename}"
client.send(request.encode())

response = client.recv(1024).decode()
print(response)

client.close()
