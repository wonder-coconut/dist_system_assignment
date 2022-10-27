import socket
import sys
import _thread
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name) #automatically detects server ip

if (len(sys.argv) != 2) :
    print("arguments syntax : <port number>")
    exit()

port = int(sys.argv[1])

server.bind((host_ip, port))
print(f"socket binded, server ip : {host_ip}:{port}")

server.listen(25)

clientList = []

def closeserver():
    input = sys.stdin.readline()
    if(input == "\close\n"):
        print('closing server')
        server.close()
        sendtochatroom('\close', None)
        os._exit(os.EX_OK)

def sendtochatroom(message, client) :
    for user in clientList :
        if (user != client) :
            try :
                user.send(bytes(message , encoding='utf-8'))
            except Exception as e :
                print('sendtochatroom() : ' + str(e))
                print('message: ' + message)
                user.close()
                clientList.remove(user)

def clientthread(client, addr):
    client.send(bytes(f"connected to chat room at : {host_ip}:{port}", encoding='utf-8'))

    while True:
        try:
            message = str(client.recv(2048), encoding= 'ascii', errors= 'ignore')
            if message:
                print("<" + addr[0] + ">:\t" + message)
                sendtochatroom("<" + addr[0] + ">:\t" + message,client) #display message to every other connected client
        
        except Exception as e:
            print('clientthread():' + str(e))
            continue

_thread.start_new_thread(closeserver, ())

while True :

    client, addr = server.accept()
    clientList.append(client)
    print(addr[0] + " added to the room")
    _thread.start_new_thread(clientthread,(client,addr)) #seperate thread for each client

