server:

run : python3 server.py <port number>

functionality :
- handles chat clients in a multi threaded system, each client on their own thread (hardcoded limit of users : 25)
- can broadcast messages to all clients (TODO : make it user accessible)
- '\close' command can cleanly shut down the server and all connected clients

client:

run : python3 client.py <server ip> <port number>

functionality :
- can independently send messages without requiring a server response for update
- '\close' command to shut down client application