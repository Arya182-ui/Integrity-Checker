from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted = fernet.encrypt(file.read())
    with open(file_path, 'wb') as file:
        file.write(encrypted)
