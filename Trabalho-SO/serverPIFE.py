import socket
import threading

'''
Servidor - cliente pront :D

Para funcionar, rode o server.py e depois o client.py

'''

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 6969
ADDR = (host, port)
DC_MSG = "!DC"

server.bind(ADDR)
server.listen()

clients = []
nicknames = []

def broadcast(msg_send):
    for client in clients:
        client.send(msg_send)
        print(msg_send.decode("ascii"))
        
def handle_client(client):
    while True:
        try:
            msg = client.recv(1024).decode("ascii")
            
            index = clients.index(client)
            nick = nicknames[index]
            
            msg_send = f"< {nick} > {msg}"
            broadcast(msg_send.encode("ascii"))
            
            if msg == DC_MSG:
                remove(client)
                break
        except:
            remove(client)
            break


def remove(client):
    index = clients.index(client)
    clients.remove(client)
    client.close()
    nick = nicknames[index]
    broadcast(f"{nick} Se desconectou :(".encode("ascii"))
    nicknames.remove(nick)


def receive():
    while True:
        client, address = server.accept()
        print(f"Conectado com {str(address)}")
        
        client.send("NEW_NICKNAME".encode('ascii'))
        nick = client.recv(1024).decode('ascii')
        
        nicknames.append(nick)
        clients.append(client)
        
        
        print(f"Nickname do cliente é {nick}")
        broadcast(f"< Server > {nick} entrou no chat!".encode("ascii"))
        client.send("< Server_PV > Conectado ao servidor, !DC para desconectar".encode('ascii'))
        
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print("[STARTING] server is starting...")
receive()