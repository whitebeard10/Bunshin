from cryptography.fernet import Fernet

# Generate a key and save it securely
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_password(password):
    encrypted_bytes = cipher_suite.encrypt(password.encode())
    return encrypted_bytes.decode("utf-8")  # Convert bytes to string

def decrypt_password(encrypted_password):
    encrypted_bytes = encrypted_password.encode("utf-8")  # Convert string to bytes
    return cipher_suite.decrypt(encrypted_bytes).decode()