from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher_suite = Fernet(key)

message = b"This is a secret message."

cipher_text = cipher_suite.encrypt(message)

plain_text = cipher_suite.decrypt(cipher_text)

print("Original Message:", message)
print("Encrypted Message:", cipher_text)
print("Decrypted Message:", plain_text.decode())
