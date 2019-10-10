import socket, select

# Broadcast de mensagens para todos os clientes
def broadcast_data(sock, message):
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock:
            try:
                socket.send(message)
            except:
                socket.close()
                CONNECTION_LIST.remove(socket)


if __name__ == "__main__":

    CONNECTION_LIST = []
    RECV_BUFFER = 4096
    HOST = 'localhost'
    PORT = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)

    # Adicionando o socket do server na lista de readable connections
    CONNECTION_LIST.append(server_socket)

    print "Servidor na porta " + str(PORT)

    while 1:
        # Select para pegar a lista de sockets que estao prontos para leitura
        read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

        for sock in read_sockets:
            # Nova conexao
            if sock == server_socket:
                # Nova conexao recebida pelo server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "Client (%s, %s) conectado" % addr

                broadcast_data(sockfd, "[%s:%s] entrou\n" % addr)

            # Mensagem do client
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)
                except:
                    broadcast_data(sock, "Client (%s, %s) esta offline" % addr)
                    print "Client (%s, %s) esta offline" % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue

    server_socket.close()