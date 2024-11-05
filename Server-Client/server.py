import socket
import threading
import sys
import select
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

HEADER = 2048
DC_MSG = "!DC"

if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    sys.exit(1)

ip_address = str(sys.argv[1])
port = int(sys.argv[2])
ADDR = (ip_address, port)


#conecta o socket a um endereço e porta
server.bind(ADDR)
list_clients = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("Welcome to the chatroom!!")
    
    connected = True
    while connected:
        msg = conn.recv(HEADER)
        if msg:   
            msg_send = f"< {addr} > {msg}"
            print(msg_send)

            broadcast(msg_send, conn)
            
            if msg == DC_MSG:
                connected = False
                
            #conn.send("Message received".encode(FORMAT))
    conn.close()
        
def broadcast(msg_send, conn):
    for client in list_clients:
        if client != conn:
            try:
                client.send(msg_send)
            except:
                list_clients.remove(client)
                print(f"[DISCONNECTED] {client}")
                client.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {ADDR[0]}")
    while True:
        conn, addr = server.accept()
        list_clients.append(conn)
        print(f"{addr[0]} connected") 
        thread = threading.Thread(target = handle_client, args =(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
            
print("[STARTING] server is starting...")
start()

server.close()

#para funcionar, primeiro rodar o server.py no VS code mesmo, CTRL + F5
# e depois rodar o client.py no terminal, python client.py, na mesma pasta do server.py 