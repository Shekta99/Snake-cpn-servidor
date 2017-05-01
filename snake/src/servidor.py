import socket

s = socket.socket()
s.bind(("localhost", 8887))
s.listen(1)

sc, addr = s.accept()
print 'esperando'
puntos = sc.recv(1024)
mesage=input("Puntos:"+ str(puntos))
sc.send(mesage)
sc.close()
