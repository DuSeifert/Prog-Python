import socket
import select
import sys
import threading

HEADER = 16
DC_MSG = "!DC"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

ip_address = str(sys.argv[1])
port = int(sys.argv[2])
ADDR = (ip_address, port)
client.connect(ADDR)

def handle_stdin(client):
    while True:
        msg = sys.stdin.readline()
        client.send(msg)
        sys.stdout.write(f"<You> {msg}")
        sys.stdout.flush()
  
connected = True
threading.Thread(target=handle_stdin, args=(client,)).start()
while connected:
    socket_list = [sys.stdin, client]
    try:
        read_sockets, write_socket, error_socket = select.select(socket_list, [], [])
    except Exception as e:
        print(f"Error with select: {e}")
        sys.exit(1)
        
    for socks in read_sockets:
        if socks == client:
            message = socks.recv(2048)
            print(message)

msg = ""
while msg != DC_MSG:
    msg = input("Escreva alguma coisa (!DC para desconectar): ")
    client.send(msg)


#para funcionar, primeiro rodar o server.py no VS code mesmo, CTRL + F5
# e depois rodar o client.py no terminal, 'python client.py', na mesma pasta do server.py