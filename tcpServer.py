import socket

miSocket = socket.socket()
miSocket.bind(('localhost',8000))
miSocket.listen(10)

while True:
    conn,addr = miSocket.accept()#retorna 2 valores la conexion y la direccion y las guada en las variables.
    print ("Nueva conexion establecida")
    print (addr)

    message = 'Hola, saludos desde el servidor'

    conn.send(message.encode())
    conn.close()