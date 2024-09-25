
from cryptography.fernet import Fernet

# secret_key = Fernet.generate_key()

secret_key = b'kLfFejwgfNUpIoWPO8CeEpqB5U-djc_M-yj_7j0z_AA='

text = 'Metin Qardasov'

crypto = Fernet(secret_key)

# encrypted_text = crypto.encrypt(text.encode())
encrypted_text = b'gAAAAABm0gWIwnfchtN9Py8prpQuFiEx2GsQPJGTkH-1cYyPbS3S09yQeIPJJRJZQak1okZxz-5DLUSOneSsk_gBgKR9lLu7Wg=='


crypto = Fernet(secret_key)
decrypted_text = crypto.decrypt(encrypted_text)
print(decrypted_text.decode())