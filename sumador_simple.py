#!/usr/bin/python3

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost',1234))

mySocket.listen(5)

primer_sumando = True

try:
	while True:

		print('Waiting for conections')
		(recvSocket, address) = mySocket.accept()
		print('HTTP request received:')
		request = recvSocket.recv(1024).decode('utf-8')
		print(request)

		sumando = request.split()[1][1:]

		if sumando == "favicon.ico":
			recvSocket.send(bytes("HTTP/1.1 404 Not Found OK \r\n\r\n", 'utf-8'))
		try:
			sumando = int(sumando)
		
		except:
			print("sumando no valido")
			recvSocket.send(bytes("HTTP/1.1 T 200 OK \r\n\r\n" + 
									"<html><body><h1> "+str(sumando)+" no valido. Introduzca un numero valido"	
									"</h1></body></html>",'utf-8'))
			recvSocket.close()
			continue
	

		if primer_sumando:
			print("primer sumando:" + str(sumando))
			sumando1 = sumando
			recvSocket.send(bytes("HTTP/1.1 200 OK \r\n\r\n" + 
								"<html><body><h1>Primer sumando: " + 
								str(sumando1) + 
								"</h1></body></html>", 'utf-8'))
			recvSocket.close()
			primer_sumando = False
		else:
			#print("segundo sumando:" + str(sumando)
			suma = sumando1 + sumando
			print("suma :" + str(suma))
			recvSocket.send(bytes("HTTP/1.1 200 OK \r\n\r\n" + 
									"<html><body><h1>Resultado: " +
									str(sumando1) + "+" + str(sumando) + "=" + 
									str(suma) + 
									"</h1></body></html>", 'utf-8'))
			recvSocket.close()
			primer_sumando = True
			continue

except KeyboardInterrupt:
	print("FIN")
	
