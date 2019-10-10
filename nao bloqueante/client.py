import socket, select, string, sys

def prompt():
    sys.stdout.write('<Voce> ')
    sys.stdout.flush()

if __name__ == "__main__":

    if (len(sys.argv) < 3):
        print 'O chat encerra se uma mensagem vazia for enviada'
        sys.exit()

    HOST = 'localhost'
    PORT = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # Conectando
    try:
        s.connect((HOST, PORT))
    except:
        print 'Impossivel conectar'
        sys.exit()

    print 'Conectado! Pode mandar mensagens!'
    prompt()

    while 1:
        socket_list = [sys.stdin, s]

        # Lista de sockets para leitura
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            # mensagem do server
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print '\nDesconectado'
                    sys.exit()
                else:
                    # print data
                    sys.stdout.write(data)
                    prompt()

            # usuario mandou uma mensagem
            else:
                msg = sys.stdin.readline()
                s.send(msg)
                prompt()