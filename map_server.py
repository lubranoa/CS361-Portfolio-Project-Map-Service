# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/28/2022
# Description: This Python socket server will listen for connections and
#     messages from connected clients, which can only be a string consisting
#     of a set of coordinates or a disconnect message. The coordinates in the
#     message string are incorporated into a Mapbox Static Images API request
#     URL, which is then sent back to the connected client socket program. This
#     URL can then be placed in the src property of an HTML img element to
#     display a static satellite image of the sent coordinates.
#
# -----------------------------------------------------------------------------

import socket
import threading
from static_map_mapbox import get_map_req_url

MSG_SIZE = 2048
FORMAT = 'utf-8'
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5678
DISCONNECT_MSG = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


def handle_map_client(conn, addr):
    """
    Handles incoming messages from clients. Message can only be a string of the
    form "latitude,longitude", i.e. "33.5277,-112.262608" or the specified
    disconnect message. Does not validate messages yet.

    Sends a Mapbox Static Images API request URL back to the client that can
    be added as a src property to an HTML img element on a web page

    :param conn: connection object to a client
    :param addr: address of client
    :return: Sends a URL string to connected client
    """
    print(f'New Connection from {addr}\n')
    connected = True
    while connected:
        msg_len = conn.recv(MSG_SIZE).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            print(f"{addr}: {msg}")
            if msg == DISCONNECT_MSG:
                connected = False
            else:
                if msg[-1] == ',':
                    msg = msg[:-1]
                map_coord = msg.split(',')
                # calls function from static_map_box.py to generate URL
                img_url = get_map_req_url(map_coord)
                print('img url:', img_url)
                conn.send(img_url.encode(FORMAT))
    conn.close()


def start():
    """Starts the server and starts new threads for each incoming connection"""
    server.listen()
    print(f"Server listening on IP {HOST}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_map_client, args=(conn, addr))
        thread.start()
        print(f"Active Connections: {threading.active_count() - 1}")


print(f"Server starting on Port {PORT}...")
start()
