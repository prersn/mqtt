# MQTT Client-Server Communication

This repository contains code for setting up an MQTT client-server communication system. MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol widely used for IoT (Internet of Things) and other messaging applications.

## Prerequisites

Before running the MQTT client and server, ensure you have the following dependencies installed:

- Python 3.x
- Paho MQTT library (`paho-mqtt`)
- Cryptography library (`cryptography`)

You can install the dependencies using pip:
`pip install paho-mqtt cryptography`


## Setting Up

### MQTT Broker

1. **Choose an MQTT Broker**: You can use any MQTT broker of your choice. In this example, we'll use `mqtt.eclipseprojects.io`.

2. **Configure TLS/SSL (Optional)**: If your MQTT broker requires SSL/TLS connection, make sure to set up the appropriate certificate (e.g., `mosquitto.crt`). Update the path in `sub.py` and `pub_cn.py` accordingly.

### MQTT Client

1. **Clone the Repository**: Clone this repository to your local machine where you intend to run the MQTT client. Run the following command:

`git clone <repository_url>`


Replace `<repository_url>` with the URL of this repository.

2. **Run the Client**: Open a terminal and navigate to the directory containing the `sub.py` file.

3. **Execute the Client**: Run the following command to start the MQTT client:

`python sub.py`


4. **Subscribe to a Topic**: When prompted, enter the topic you want to subscribe to. Ensure that the topic matches the one published by the server.

### MQTT Server

1. **Clone the Repository**: Clone this repository to your local machine where you intend to run the MQTT server. Run the following command:

`git clone <repository_url>`


Replace `<repository_url>` with the URL of this repository.

2. **Run the Server**: Open a terminal and navigate to the directory containing the `pub_cn.py` and `pub_daa.py` files.

3. **Execute the Server**: Run the following command to start the MQTT server:

`python pub_cn.py`
or
`python pub_daa.py`


4. **Enter Task Information**: Follow the prompts to enter the number of tasks and their corresponding messages. The server will publish encrypted data to the specified MQTT topic.

## Notes

- Ensure that both the MQTT client and server have network connectivity to the MQTT broker.
- Adjust the MQTT broker details in the code if you're using a different broker.
- Use secure methods to manage and distribute encryption keys.
- Feel free to modify the code to suit your specific requirements.

