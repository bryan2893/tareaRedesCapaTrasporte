import socket
import os
dirname = os.path.dirname(__file__)

# Funcion para escribir el archivo en la carpeta files del cliente--->Download funtionality.


def writeFileComesFromServer(codedData):
    try:
        fileName = input("Type file name to save: ")
        file = open(os.path.join(dirname, "../files/"+fileName+".txt"), 'wb')
        file.write(codedData)
        file.close()
        print("File has been recorded!")
    except Exception as e:
        print(e)


def sendFileToServer(socket, fileName):
    return ""


def connectToTcp(arrayOfParams):
    ipAddres, port, action, fileName = arrayOfParams[1], arrayOfParams[2], arrayOfParams[3], arrayOfParams[4]

    # At this point i'm sure arrayOfParams are correct because have been evaluated before sending
    portNumber = int(port)

    mi_socket = socket.socket()
    mi_socket.connect((ipAddres, portNumber))
    print("connection to tcp server was done succesfully!")

    if (action == "-u"):
        # obtener el archivo para subirlo al servidor...
        print("Subiendo al servidor...")
    else:
        message = action+" "+fileName

        if(action == "-d"):
            mi_socket.send(message.encode())
            respuesta = mi_socket.recv(1024)#Se recibe un archivo desde el servidor.

            #La respuesta no se decodifica ya que lo que viene es un archivo.
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
