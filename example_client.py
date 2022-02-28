# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/27/2022
# Description: This program
#
# -----------------------------------------------------------------------------

import socket

MSG_SIZE = 2048
FORMAT = 'utf-8'
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
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
    print(client.recv(MSG_SIZE).decode(FORMAT))


send('Hello World!')
send(DISCONNECT_MSG)
