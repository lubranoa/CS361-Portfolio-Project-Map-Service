# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/27/2022
# Description: This program
#
# -----------------------------------------------------------------------------

import socket
import threading

MSG_SIZE = 2048
FORMAT = 'utf-8'
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
DISCONNECT_MSG = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


def handle_map_client(conn, addr):
    """Does this"""
    print(f'New Connection from {addr}.\n')
    connected = True
    while connected:
        msg_len = conn.recv(MSG_SIZE).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"{addr}: {msg}")
            conn.send("Message Received".encode(FORMAT))

    conn.close()


def start():
    """Does this"""
    server.listen()
    print(f"Server listening on IP {HOST}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_map_client, args=(conn, addr))
        thread.start()
        print(f"Active Connections: {threading.active_count() - 1}")


print(f"Server starting on Port {PORT}...")
start()
