# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/28/2022
# Description: This is a basic client example. It sends a string of coordinates
#     of the form "latitude,longitude", i.e. "33.5277,-112.262608" and receives
#     a Mapbox Static Images API request URL from the running socket server.
#
# -----------------------------------------------------------------------------

import socket

MSG_SIZE = 2048
FORMAT = 'utf-8'
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5678
DISCONNECT_MSG = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(msg)
    send_length = str(msg_len).encode(FORMAT)
    send_length += b' ' * (MSG_SIZE - len(send_length))
    client.send(send_length)
    client.send(message)
    img_url = client.recv(MSG_SIZE).decode(FORMAT)
    print(img_url)
    # return img_url


send('33.5277,-112.262608')
# print(response)
send(DISCONNECT_MSG)
