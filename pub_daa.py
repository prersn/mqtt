import paho.mqtt.client as mqtt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os 
import time

def encrypt(message, key):
    key = key.ljust(16)[:16]
    cipher = Cipher(algorithms.AES(key), modes.CFB(b'\x00'*16), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

n = int(input("Enter the number of tasks under this topic: "))
i = 0
while i < n:
    tasks_message1 = input(f"Enter message for task {i + 1}: ")
    encrypted_data1 = encrypt(tasks_message1.encode("utf-8"), b'your_secret_key')
    client.publish("daa", encrypted_data1)
    print(f"Just published encrypted data for task {i + 1} to Topic daa")
    time.sleep(1)
    i = i + 1
