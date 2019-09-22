import socket

#mi_socket = socket.socket()
#mi_socket.connect(('localhost',8000))

#message = 'Hola desde el ciente'
#mi_socket.send(message.encode())

#respuesta = mi_socket.recv(1024)
#respuesta.decode()

#print(respuesta)
#mi_socket.close()

PROGRAM_NAME = 'tcpServer'
VALID_ACTIONS = ['-d','-u','-l']

def isValidAction(action):#action can be -d -u or -l ¡no more!.
    for actionElement in VALID_ACTIONS:
        if(actionElement == action):
            return True
    return False

def isNumber(string):
    numero = string
    try:
        int(numero) - 6
        return True
    except:
        return False


def validateCommandSyntax(paramsArray):
    if( len(paramsArray) < 5 or len(paramsArray) > 5):
        raise Exception("Error: 5 parameters are required, you only typed "+str(len(paramsArray))+"!")
    if(paramsArray[0] != PROGRAM_NAME):
        raise Exception("Error: Command must begin with 'tcpServer' keyword!")
    if(not isNumber(paramsArray[2])):
        raise Exception("Error: Third parameter have to be a valid port!")
    if(not isValidAction(paramsArray[3])):
        raise Exception("Error: Fourth parameter must be only -d,-u or -l")
    
    return True
    

def callServer(paramsArray):
    try:
        if(validateCommandSyntax(paramsArray)):
            #Hacer llamada al servidor!
            print("Llamando al servidor...")
            return True
    except Exception as e:
        print(str(e))
        return False

def CommandExecutor():
    while True:
        print("Please type a command with this format: tcpServer [ipAddres] [portNumber] [action] [fileName]\n")
        command = input("Type command or press 1 to go main menu: ")
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

#startProgram()
#print(validateCommandSyntax(['tcpServer','localhost','8000','-d','nombreArchivo']))
#callServer(['tcpServer','localhost','8000','-d','nombreArchivo'])
startProgram()