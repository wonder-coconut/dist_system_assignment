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

    readsocket, writesocket, errorsocket = select.select(socketlist, [], []) #server socket or terminal input for message

    for socket in readsocket:
        if (socket == server) : #server message incoming
            message = str(socket.recv(2048), encoding= 'ascii', errors= 'ignore')
            if(message == '\close'):
                server.close()
                exit()
            print(message)

        else : #client message outgoing
            message = sys.stdin.readline()
            if(message == '\close\n'):
                server.close()
                exit()
            server.send(bytes(message, 'utf-8'))
            print('<host>\t' + message)