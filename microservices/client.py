# we can build a socket client
import socket
def client():
    '''this is a basic socket client to interact with our socket server'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_t = ('localhost', 9874)
    # connect to the server
    client.connect(port_t)
    # send a message to the server
    client.send( 'hello'.encode() )
    # if anything comes back from the server, handle it here
    data = client.recv(1024)
    print(f'Client received {data}')
    client.close()

if __name__ == '__main__':
    client()