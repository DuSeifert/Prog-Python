import socket

HEADER = 16
PORT = 6969
FORMAT = "utf-8"
DC_MSG = "!DC"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    mensagem = msg.encode(FORMAT)
    msg_length = len(mensagem)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' *(HEADER - len(send_length))
    client.send(send_length)
    client.send(mensagem)
    print(client.recv(2048).decode(FORMAT))
    
send("Hello World!")
input()
send(DC_MSG)

#para funcionar, primeiro rodar o server.py no VS code mesmo, CTRL + F5
# e depois rodar o client.py no terminal, 'python client.py', na mesma pasta do server.py