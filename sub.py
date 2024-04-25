import paho.mqtt.client as mqtt
import ssl
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def decrypt(ciphertext, key):
    key = key.ljust(16)[:16]
    cipher = Cipher(algorithms.AES(key), modes.CFB(b'\x00'*16), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    return unpadded_data

def on_message(client, userdata, message):
    try:
        secret_key = b'your_secret_key'
        decrypted_data = decrypt(message.payload, secret_key)
        print("Received decrypted message on topic '{}': {}".format(message.topic, decrypted_data.decode("utf-8")))
    except Exception as e:
        print(f"Error processing message: {str(e)}")

mqttBroker = "mqtt.eclipseprojects.io"

topic = input("Enter the topic to subscribe to: ")

tls_context = ssl.create_default_context()
tls_context.load_verify_locations(cafile=r"mosquitto.crt")

client = mqtt.Client("Smartphone")
client.tls_set_context(context=tls_context)

try:
    client.connect(mqttBroker, port=8883)
except Exception as e:
    print(f"Error connecting to MQTT broker: {str(e)}")
    exit()

client.loop_start()
client.subscribe(topic)

try:
    time.sleep(30)
except KeyboardInterrupt:
    pass

client.loop_stop()
