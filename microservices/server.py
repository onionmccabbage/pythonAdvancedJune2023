# we can build a socket server
import socket # this provides all we need for socket programming
from datetime import datetime
def server():
    '''this microservice will listen for request, respond to request
       and be available over an http port '''
    # here are some good defaults for a microservice
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # we need some port settings
    port_t = ('localhost', 9874) # or a fixed IP address
    server.bind(port_t)
    # set our server to listen
    server.listen(4) # listen for up to 4 clients
    print(f'Server is running on {port_t[0]} port {port_t[1]}')
    # we need a run loop
    while True:
        # unpack any request we may recieve
        (client, addr) = server.accept()
        print(f'request received from {addr}')
        # read the first 1024 bytes of the buffer
        buf = client.recv(1024)
        # we can choose to send a response
        print(f'Server received {buf}')
        if buf==b'date':
            date = datetime.now()
            client.send( f'{date}'.encode() ) # we would format the date
        elif buf==b'time':
            time = datetime.now().strftime("%H:%M:%S")
            client.send( f'{time}'.encode() ) # we would format the time
        else:        
            client.send( buf.upper() ) # send it back in upper case
        client.close()
        # if the client sends b'quit' then we will close the server
        if buf == b'quit':
            print('server is closing')
            server.close()
            break
        

if __name__ == '__main__':
    server()