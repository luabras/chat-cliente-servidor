import socket
import sys
from thread import *

HOST = 'localhost'
PORT = 5000

x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket criado'

try:
    x.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind falhou. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

x.listen(10)
print 'Socket now listening'

# Criar threads
def clientthread(conn):

    while True:
        # Recebendo do client
        data = conn.recv(1024)

        if not data:
            break

        conn.send(data)

    conn.close()

while 1:
    # esperando a conexao ser aceita
    conn, addr = x.accept()
    print 'Conectado com ' + addr[0] + ':' + str(addr[1])

    start_new_thread(clientthread, (conn,))

x.close()