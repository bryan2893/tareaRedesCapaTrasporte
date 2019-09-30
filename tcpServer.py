import socket
import os
dirname = os.path.dirname(__file__)


miSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
miSocket.bind(('localhost', 8000))
miSocket.listen(10)

# Obtiene lista de archivos del servidor...

def getListOfFiles():
    fileNamesArray = []
    pathi = os.path.join(dirname, "serverFiles")
    for file_names in os.walk(pathi):
        fileNamesArray = file_names[2]

    namesString = ""
    i = 0
    while (i < len(fileNamesArray)):
        namesString += fileNamesArray[i]
        if(i+1 != len(fileNamesArray)):
            namesString += ","
        i += 1

    return namesString


def existFile(fileName):
    fileNamestring = getListOfFiles()
    arrayFileList = fileNamestring.split(",")

    requestedFile = commandsArray[1]
    for fileName in arrayFileList:
        if (fileName == requestedFile):
            return True
    return False

def writeFileComesFromClient(fileName,codedData):
    try:
        file = open(os.path.join(dirname, "serverFiles/"+fileName), 'wb')
        file.write(codedData)
        file.close()
        print("File has been recorded!")
    except Exception as e:
        print(e)


while True:
    # retorna 2 valores la conexion y la direccion y las guarda en las variables.
    conn, addr = miSocket.accept()
    print("Nueva conexión establecida!")
    print(addr)

    data = conn.recv(1024)
    if(data):
        dataReceived = data.decode()

        commandsArray = dataReceived.split()

        if commandsArray[0] == "-l":
            listOfFiles = getListOfFiles()
            conn.send(listOfFiles.encode())

        elif(commandsArray[0] == "-d"):
            fileName = commandsArray[1]
            if(existFile(fileName)):
                print("Sending file to client...")
                try:
                    fileN = open(os.path.join(dirname, "serverFiles/"+fileName),'br')
                    readedFile = fileN.read()
                    conn.send(readedFile)
                    fileN.close()
                    print("File sended succesfully!")
                except Exception as e:
                    print(e)
            else:
                # Avisar que el archivo no existe en el servidor.
                print("")

        else:  # Se subirá un archivo...
            filename = commandsArray[1]
            print(filename)
            conn.send(filename.encode())

            response = conn.recv(1024)
            if(response):
                writeFileComesFromClient(filename,response)

            print("Se subio un archivo al servidor!")
            
            #message = 'Los datos se recibieron bien!'
            # conn.send(message.encode())

    conn.close()