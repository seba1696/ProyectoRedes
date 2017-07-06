import socket

s = socket.socket()
s.connect(('127.0.0.1', 9999))
while True:
	mensaje = raw_input('>>> ')
	s.sendall(mensaje)
	if mensaje == 'quit':
		break
print 'adios'
s.close()	
