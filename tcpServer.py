import socket
import os
dirname = os.path.dirname(__file__)


miSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
miSocket.bind(('localhost',8000))
miSocket.listen(10)

#Obtiene lista de archivos del servidor...
def getListOfFiles():
    fileNamesArray = []
    pathi = os.path.join(dirname, "serverFiles")
    for file_names in os.walk(pathi):
        fileNamesArray = file_names[2]

    namesString = ""
    i=0
    while (i<len(fileNamesArray)):
        namesString += fileNamesArray[i]
        if(i+1 != len(fileNamesArray)):
            namesString += ","
        i+=1
    
    return namesString

while True:
    conn,addr = miSocket.accept()# retorna 2 valores la conexion y la direccion y las guarda en las variables.
    print ("Nueva conexión establecida!")
    print (addr)

    data = conn.recv(1024)
    if(data):
        dataReceived = data.decode()

        commandsArray = dataReceived.split()

        if commandsArray[0] == "-l":
            listOfFiles = getListOfFiles()
            conn.send(listOfFiles.encode())

    #message = 'Los datos se recibieron bien!'
    #conn.send(message.encode())

    conn.close()