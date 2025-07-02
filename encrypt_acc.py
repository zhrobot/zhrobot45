from cryptography.fernet import Fernet

# 生成密钥
key = Fernet.generate_key()
cipher = Fernet(key)

# 读取明文 acc.txt 文件
with open('acc.txt', 'r', encoding='utf-8') as f:
    plaintext = f.read().encode('utf-8')

# 加密数据
encrypted_data = cipher.encrypt(plaintext)

# 保存加密后的数据到 acc_encrypted.txt
with open('acc_encrypted.txt', 'wb') as f:
    f.write(encrypted_data)

# 保存密钥到 key.key
with open('key.key', 'wb') as f:
    f.write(key)

print("加密完成！加密文件保存为 'acc_encrypted.txt'，密钥保存为 'key.key'。请妥善保管密钥文件！")