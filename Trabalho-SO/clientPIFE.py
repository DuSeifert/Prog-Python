import socket
import threading

'''
Servidor - cliente pront :D

Para funcionar, rode o server.py e depois o client.py

'''

'''
TODO:
    - Testar a comunicação com um jogo simples de pedra, papel e tesoura
    - Se tudo estiver funcionando, implementar um jogo de PIFE
    - Criar o jogo em si
    - Integrar o jogo com o servidor
    - Tirar nota máxima >:D
'''

nickname = input("\n\n< Server_PV > Escolha um nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 6969
ADDR = (host, port)

client.connect(ADDR)

DC_MSG = "!DC"
connected = True


def receive():
    global connected
    while connected:
        try:
            msg = client.recv(1024).decode('ascii')
            if msg == "NEW_NICKNAME":
                client.send(nickname.encode('ascii'))
            else:
                print(msg)
        except:
            print("Ocorreu um erro")
            client.close()
            connected = False
            exit(1)
            break
                    
        
def write():
    global connected
    while connected:
        try:
            msg = input('')
            client.send(msg.encode('ascii'))
            if msg == DC_MSG:
                client.close()
                connected = False
                exit(1)
                break
            
        except:
            print("Ocorreu um erro")
            client.close()
            connected = False
            exit(1)
            break
        

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()