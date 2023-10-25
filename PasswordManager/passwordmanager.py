from cryptography.fernet import Fernet
import sqlite3

def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open('key.key', 'rb').read()

def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

def initialize_database():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS passwords (service TEXT, password TEXT)')
    conn.commit()
    conn.close()

def store_password(service, password, key):
    encrypted_password = encrypt_password(password, key)
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO passwords VALUES (?, ?)', (service, encrypted_password))
    conn.commit()
    conn.close()

def retrieve_password(service, key):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM passwords WHERE service = ?', (service,))
    result = cursor.fetchone()
    conn.close()

    if result:
        encrypted_password = result[0]
        decrypted_password = decrypt_password(encrypted_password, key)
        return decrypted_password
    else:
        return None

if __name__ == "__main__":
    generate_key()  
    key = load_key()
    initialize_database()

    while True:
        print("Options:")
        print("1. Store Password")
        print("2. Retrieve Password")
        print("3. Quit")
        choice = input("Enter option: ")

        if choice == '1':
            service = input("Enter the service: ")
            password = input("Enter the password: ")
            store_password(service, password, key)
            print("Password stored successfully!")
        elif choice == '2':
            service = input("Enter the service: ")
            password = retrieve_password(service, key)
            if password:
                print(f"Password for {service}: {password}")
            else:
                print(f"No password found for {service}.")
        elif choice == '3':
            break
