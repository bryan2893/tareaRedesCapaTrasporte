import socket

#se importa el modulo de validaciones para la simulacion de linea de comandos.
from service.validations import validateCommandSyntax,TCP_SERVER_NAME,UDP_SERVER_NAME
from service.tcpClient import connectToTcp
from service.udpClient import connectToUDP

#mi_socket = socket.socket()
#mi_socket.connect(('localhost',8000))

#message = 'Hola desde el ciente'
#mi_socket.send(message.encode())

#respuesta = mi_socket.recv(1024)
#respuesta.decode()

#print(respuesta)
#mi_socket.close()

def callServer(paramsArray):
    try:
        if(validateCommandSyntax(paramsArray)):
            #Hacer llamada al servidor UDP O TCP!
            if(paramsArray[0] == TCP_SERVER_NAME):
                print("Llamando al servidor TCP...")
                connectToTcp(paramsArray)
            if(paramsArray[0] == UDP_SERVER_NAME):
                connectToUDP(paramsArray)
    except Exception as e:
        print(str(e))

def CommandExecutor():
    while True:
        print("Please type a command with this format: [tcpServer or udpServer] [ipAddres] [portNumber] [action] [fileName]\n")
        command = input("Type command or press 1 to go back main menu: ")
        if(command == "1"):
            break
        else:
            paramsArray = command.split()
            callServer(paramsArray)

def startProgram():
    while True:
        print("1) Execute command\n2) Exit\n")
        choosedOption = input("Choose an option: ")
        print("\n")
        if(choosedOption == "1"):
            CommandExecutor()
        if(choosedOption == "2"):
            break

    print("Exit with status code 0!")


startProgram()