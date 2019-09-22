import socket

#Funcion para hacer llamadas al servidor tcp
miSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
miSocket.bind(('localhost',8000))
miSocket.listen(10)

while True:
    conn,addr = miSocket.accept()#retorna 2 valores la conexion y la direccion y las guarda en las variables.
    print ("Nueva conexion establecida!")
    print (addr)

    data = conn.recv(1024)
    if(data):
        print(data.decode())

    #message = 'Los datos se recibieron bien!'
    #conn.send(message.encode())

    conn.close()