import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT  = 5050

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((SERVER,PORT))

def client_hand(conn,addr):
    count = 0
    print(f'[ADDED] {addr}')
    connected = True
    while connected:
        count = count+1
        if count == 1:
            name = conn.recv(512).decode()
        msg = conn.recv(512).decode()
        if msg == '!DIS':
            connected = False
            print(f'{name} has left the server')
        else:
    
                print(name,':',msg)   
def main_server():
    server_socket.listen()
    print(F'[LISTENING] ON {SERVER}')
    while True:
        conn,addr = server_socket.accept()
        thread = threading.Thread(target=client_hand,args=[conn,addr])
        thread.start()
main_server()
