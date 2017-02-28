#!/usr/bin/python3

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost',1234))

mySocket.listen(5)

primer_sumando = True
while True:

	print('Waiting for conections')
	(recvSocket, address) = mySocket.accept()
	print('HTTP request received:')
	request = recvSocket.recv(1024).decode('utf-8')
	print(request)

	sumando = (request.split())[1][1:]
	try: 
		if primer_sumando:
			print("primer sumando:" + sumando)
			sumando1 = int(sumando)
			recvSocket.send(bytes("HTTP/1.1 200 OK \r\n\r\n" + 
								"<html><body><h1>Primer sumando: " + sumando1 + "</h1></body></html>", 'utf-8'))

		else:
			print("segundo sumando:" + sumando)
			suma = sumando1 + sumando
			print("suma :" + int(suma))
			recvSocket.send(bytes("HTTP/1.1 200 OK \r\n\r\n" + 
								"<html><body><h1>Resultado: " + int(suma) + "</h1></body></html>", 'utf-8'))
		
		primer_sumando = False
		
	except:
		if primer_sumando == "favicon.ico":
			"None"
	

recvSocket.close()

