TCP_SERVER_NAME = 'tcpServer'
UDP_SERVER_NAME = 'udpServer'
VALID_ACTIONS = ['-d','-u','-l']
VALID_KEYWORDS = [TCP_SERVER_NAME,UDP_SERVER_NAME]

def isValidKeyword(keywordByParameter):
    for keyword in VALID_KEYWORDS:
        if(keyword == keywordByParameter):
            return True
    return False

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
    if(not isValidKeyword(paramsArray[0])):
        raise Exception("Error: Command must begin with '"+TCP_SERVER_NAME+"' or '"+UDP_SERVER_NAME+"' keyword!")
    if(not isNumber(paramsArray[2])):
        raise Exception("Error: Third parameter have to be a valid port!")
    if(not isValidAction(paramsArray[3])):
        raise Exception("Error: Fourth parameter must be only -d,-u or -l")
    
    return True