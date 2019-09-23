import socket
import os
dirname = os.path.dirname(__file__)

#Funcion para escribir el archivo en la carpeta files del cliente
def writeFileComesFromServer(codedData):
    try:
        fileName = input("Type file name to save: ")
        file = open(os.path.join(dirname,"../files/"+fileName+".txt"),'wb')
        file.write(codedData)
        file.close()
        print("File has been recorded!")
    except Exception as e:
        print(e)

def sendFileToServer():
    return ""

def connectToTcp(arrayOfParams):
    ipAddres,port,action,fileName = arrayOfParams[1],arrayOfParams[2],arrayOfParams[3],arrayOfParams[4]

    #At this point i'm sure arrayOfParams are correct because have been evaluated before sending
    portNumber = int(port)

    mi_socket = socket.socket()
    mi_socket.connect((ipAddres,portNumber))
    print("connection to tcp server was done succesfully!")

    message = action+" "+fileName
    mi_socket.send(message.encode())
    
    respuesta = mi_socket.recv(1024)
    writeFileComesFromServer(respuesta)

    mi_socket.close()