import socket  # para socket
import sys  # para saida

def prompt():
    sys.stdout.write('<Voce> ')
    sys.stdout.flush()

if __name__ == "__main__":

    if (len(sys.argv) < 3):
        print 'O chat encerra se uma mensagem vazia for enviada'
        sys.exit()

HOST = 'localhost'
PORT = 5000

y = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
y.settimeout(2)

# Conectando
try:
    y.connect((HOST, PORT))
except:
    print 'Impossivel conectar'
    sys.exit()

print 'Conectado! Pode mandar mensagens!'
prompt()

while True:
    msg = sys.stdin.readline()
    y.send(msg)
    prompt()

y.close()