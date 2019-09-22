import socket
import os
dirname = os.path.dirname(__file__)
#filename = os.path.join(dirname, '../serverFiles/archivo.txt')

#Funcion para escribir el archivo en la carpeta serverFiles
def writeFileComesFromServer(codedData):
    #file = open(os.path.join(dirname, '../serverFiles/archivo.txt'))
    try:
        fileName = input("Type file name to save: ")
        file = open(os.path.join(dirname,"../serverFiles/"+fileName+".txt"),'wb')
        file.write(codedData)
        file.close()
        print("File have been recorded!")
    except Exception as e:
        print(e)

def connectToTcp(arrayOfParams):
    ipAddres,port,action,fileName = arrayOfParams[1],arrayOfParams[2],arrayOfParams[3],arrayOfParams[4]

    #At this point i'm sure arrayOfParams are correct because have been evaluated before sending
    portNumber = int(port)

    mi_socket = socket.socket()
    mi_socket.connect((ipAddres,portNumber))
    print("connection to tcp server was done succesfully!")

    print("Sendind information...")
    message = action+" "+fileName
    mi_socket.send(message.encode())
    print("Information sended!")

    respuesta = mi_socket.recv(1024)
    writeFileComesFromServer(respuesta)
    #respuesta.decode()

    #print(respuesta)

    mi_socket.close()