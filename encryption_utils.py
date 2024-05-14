from cryptography.fernet import Fernet
def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data
key = Fernet.generate_key()
original_data = "Sensitive data"
encrypted_data = encrypt_data(original_data, key)
print("Encrypted data:", encrypted_data)
decrypted_data = decrypt_data(encrypted_data, key)
print("Decrypted data:", decrypted_data)