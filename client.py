import socket

PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DIS"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print('CONNECTED')
count = 0

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)

name = input('ENTER NAME : ')
send(name)

while True:
    count = count+1
    msg = input('ENTER THE MESSAGE: ')
    if msg == '!DIS':
        break
    send(msg)

send(DISCONNECT_MESSAGE)
client.close()