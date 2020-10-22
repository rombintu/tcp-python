import socket

sock = socket.socket()
sock.connect(('localhost', 9091))
sock.send(b'hello, world!')


sock.close()
