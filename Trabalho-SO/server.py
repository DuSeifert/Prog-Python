import socket
import threading

HEADER = 16
PORT = 6969
#my public ip address (to make the server work over the internet and not only on my wifi)
#177.183.212.47
#SERVER = "100.64.202.50"

#my local ip address (to make the server work only on my wifi)
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DC_MSG = "!DC"

#cria um socket, AF_INET significa a categoria do socket, que seria IPV4
#SOCK_STREAM significa que é um socket de conexão TCP (transmission control protocol)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conecta o socket a um endereço e porta
server.bind(ADDR)
list_clients = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:   
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
    
            if msg == DC_MSG:
                connected = False
            
            msg_send = f"[{addr}] {msg}"
            print(msg_send)
            broadcast(msg_send, conn)
    conn.close()
        
def broadcast(msg_send, conn):
    for client in list_clients:
        if client != conn:
            try:
                client.send(msg_send.encode(FORMAT))
            except:
                print(f"[DISCONNECTED] {client}")
                client.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        list_clients.append(conn)
        thread = threading.Thread(target = handle_client, args =(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
            
        

print("[STARTING] server is starting...")
start()




