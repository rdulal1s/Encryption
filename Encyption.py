from cryptography.fernet import Fernet

key = Fernet.generate_key()

msg = "SimplePythonProject - Let's keep it going".encode()

f_obj = Fernet(key)




encrypted_msg = f_obj.encrypt(msg)

print(key)

print(encrypted_msg)

decrypted_msg = f_obj.decrypt(encrypted_msg)

print(decrypted_msg)