from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(f"대칭키 : {key}")

fernet = Fernet(key)
encrypt_str = fernet.encrypt(b"wnstjr4428")

print("암호화된 문자열 : ", encrypt_str)

fernet = Fernet(key)
decrypt_str = fernet.decrypt(encrypt_str)

print("복호화된 문자열 : ", decrypt_str)

text = decrypt_str

print(text)