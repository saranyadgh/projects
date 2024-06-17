import socket
import threading

# Client settings
HOST = '127.0.0.1'  # Server address
PORT = 12345        # Server port

nickname = input("Choose your nickname: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive():
    """Receive messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'NICK':
                client_socket.send(nickname.encode('utf-8'))
            else:
                print(message)
        except Exception as e:
            print(f"Error: {e}")  # Debugging statement
            print("An error occurred!")
            client_socket.close()
            break

def write():
    """Send messages to the server."""
    while True:
        message = f'{nickname}: {input("")}'
        client_socket.send(message.encode('utf-8'))
        print(f"Sent message: {message}")  # Debugging statement

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
