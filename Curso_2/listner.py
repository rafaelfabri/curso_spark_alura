import socket
import time
HOST = 'localhost'
PORT = 3011

s = socket.socket()

s.bind((HOST, PORT))

print('Aguardando conexao na porta', PORT)

s.listen(5)

conn, address = s.accept()

print('Recebendo soliticitacao', address)

messages = [
    'Msg 1', 
    'Msg 2',
    'Msg 3',
    'Msg 4',
    'Msg 5',
    'Huhuh',
    'Eba'
    ]

for message in messages:
    message = bytes(message, 'utf-8')
    conn.send(message)
    time.sleep(4)
    
conn.close()
    