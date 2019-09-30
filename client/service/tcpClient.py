import socket
import os
dirname = os.path.dirname(__file__)

# Funcion para escribir el archivo en la carpeta files del cliente--->Download funtionality.

def getListOfFiles():
    fileNamesArray = []
    pathi = os.path.join(dirname, "../files")
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


def existFile(fileN):
    fileNamestring = getListOfFiles()
    arrayFileList = fileNamestring.split(",")

    for fileName in arrayFileList:
        if (fileName == fileN):
            return True
    return False

def writeFileComesFromServer(codedData):
    try:
        fileName = input("Type file name to save: ")
        file = open(os.path.join(dirname, "../files/"+fileName), 'wb')
        file.write(codedData)
        file.close()
        print("File has been recorded!")
    except Exception as e:
        print(e)


def connectToTcp(arrayOfParams):
    ipAddres, port, action, fileName = arrayOfParams[1], arrayOfParams[2], arrayOfParams[3], arrayOfParams[4]

    # At this point i'm sure arrayOfParams are correct because have been evaluated before sending
    portNumber = int(port)

    mi_socket = socket.socket()
    mi_socket.connect((ipAddres, portNumber))
    print("connection to tcp server was done succesfully!")

    message = action+" "+fileName

    if (action == "-u"):
        # obtener el archivo para subirlo al servidor...
        if(existFile(fileName)):
            try:
                mi_socket.send(message.encode())
                respuesta = mi_socket.recv(1024)

                if(respuesta.decode() == fileName):
                    fileN = open(os.path.join(dirname, "../files/"+fileName),'br')
                    readedFile = fileN.read()
                    mi_socket.send(readedFile)
                    fileN.close()
                    print("File sended to server!")
            except Exception as e:
                print(e)
    else:

        if(action == "-d"):
            mi_socket.send(message.encode())
            respuesta = mi_socket.recv(1024)#Se recibe un archivo desde el servidor.

            #La respuesta no se decodifica ya que lo que viene es informacion en bytes que es lo que necesitamos para grabar el archivo.
            writeFileComesFromServer(respuesta)
        else:#action = "-l" indicando que se requiere listar los acrchivos en el servidor.

            #Logica para listar archivos en el servidor.
            mi_socket.send(message.encode())
            respuesta = mi_socket.recv(1024)#Se recibe un archivo desde el servidor.
            filenames = respuesta.decode()
            fileNamesArray = filenames.split(",")
            
            print("Lista de archivos en el servidor...\n")
            for name in fileNamesArray:
                print(name+"\n")
        
    mi_socket.close()