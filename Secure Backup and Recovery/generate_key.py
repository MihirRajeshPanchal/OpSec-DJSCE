from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("server_key.key", "wb") as key_file:
    key_file.write(key)

print("Server encryption key generated and saved to 'server_key.key'")