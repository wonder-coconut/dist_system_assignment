import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if (len(sys.argv) != 3) :
    print("arguments syntax : <server ip> <port number>")
    exit()

server_ip = str(sys.argv[1])
port = int(sys.argv[2])
server.connect((server_ip, port))

while True:

    socketlist = [sys.stdin,server]

    readsocket, writesocket, errorsocket = select.select(socketlist, [], [])

    for socket in readsocket:
        if (socket == server) :
            message = socket.recv(2048)
            print(str(message, encoding= 'ascii', errors= 'ignore'))
        else :
            message = sys.stdin.readline()
            if(message == '\close\n'):
                server.close()
                exit()
            server.send(bytes(message, 'utf-8'))
            print('<host>\t' + message)
