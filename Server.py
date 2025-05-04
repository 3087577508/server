import socket
import argparse
from sys import argv

def server():
    parser=argparse.ArgumentParser()
    parser.add_argument('port', type=int, help='This is the port to connect to the server on',action='store')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    args = parser.parse_args()
    server_socket.bind(('0.0.0.0', args.port))
    server_socket.listen(1)

    while True:
        client_socket, client_address = server_socket.accept()
        try:
            while True:
                data = client_socket.recv(512)
                if not data:
                    break
                swappedtxt = data.decode().swapcase()
                client_socket.sendall(swappedtxt.encode())
        finally: 
                client_socket.close()

if __name__ == '__main__':
    server()
