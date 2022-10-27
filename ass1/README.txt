Server:
    Compilation:    gcc TCPEchoServer.c -o server.o
    Execution:      ./server.o <port number>

Client:
    Compilation:    gcc TCPEchoClient.c -o client.o
    Execution:      ./client.o <server addr> <server port>