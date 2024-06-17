import socket
import threading

# Server settings
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to listen on

# Initialize the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []
nicknames = []

def broadcast(message):
    """Send a message to all connected clients."""
    for client in clients:
        client.send(message)
    print(f"Broadcasting message: {message.decode('utf-8')}")  # Debugging statement

def handle_client(client):
    """Handle the communication with a client."""
    while True:
        try:
            message = client.recv(1024)
            if message:
                print(f"Received message: {message.decode('utf-8')}")  # Debugging statement
                broadcast(message)
        except Exception as e:
            print(f"Error: {e}")  # Debugging statement
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    """Accept new client connections."""
    while True:
        client, address = server_socket.accept()
        print(f'Connected with {str(address)}')

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print('Server is running...')
receive()
