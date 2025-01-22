#! /usr/bin/python3
from os import system, name
import sys
from click import Command, command
import docker
import signal
import socket
import re

_B = "[1m"
_N = "[22m"
_D = "[2m"
_RSTALL = "[0m"
_f_w = "[37m"
_f_y = "[33m"
_f_b = "[34m"
_f_bl = "[30m"
_f_r = "[31m"
_f_c = "[36m"
_f_g = "[32m"
_f_m = "[35m"


_f_ex_w = "[97m"
_f_ex_y = "[93m"
_f_ex_b = "[94m"
_f_ex_bl = "[90m"
_f_ex_r = "[91m"
_f_ex_c = "[96m"
_f_ex_g = "[92m"
_f_ex_m = "[95m"

_b_w = "[47m"
_b_y = "[43m"
_b_b = "[44m"
_b_bl = "[40m"
_b_r = "[41m"
_b_c = "[46m"
_b_g = "[42m"
_b_m = "[45m"


_b_rst = "[49m"
_b_ex_w = "[107m"
_b_ex_y = "[103m"
_b_ex_b = "[104m"
_b_ex_bl = "[100m"
_b_ex_r = "[101m"
_b_ex_c = "[106m"
_b_ex_g = "[102m"
_b_ex_m = "[105m"


DOCKER_URL = 'unix://var/run/docker.sock'
def logo():
    _m_cl = _f_ex_b
    _b_cl = _f_y
    print("")
    print(f"{_m_cl}╔═══╗╔╗╔╗{_b_cl}───────{_m_cl}╔═══╗{_b_cl}───{_m_cl}╔═╦╗{_b_cl}───{_m_cl}╔══╗  {_RSTALL}")
    print(f"{_m_cl}║╔═╗╠╝╚╣║{_b_cl}───────{_m_cl}║╔═╗║{_b_cl}───{_m_cl}║╔╝╚╗{_b_cl}──{_m_cl}╚╣╠╝  {_RSTALL}")
    print(f"{_m_cl}║║{_b_cl}─{_m_cl}║╠╗╔╣║╔══╦══╗║╚══╦══╦╝╚╗╔╝{_b_cl}───{_m_cl}║║╔═╗{_RSTALL}")
    print(f"{_m_cl}║╚═╝║║║║║║╔╗║══╣╚══╗║╔╗╠╗╔╣║{_b_cl}────{_m_cl}║║║╔╝{_RSTALL}")
    print(f"{_m_cl}║╔═╗║║╚╣╚╣╔╗╠══║║╚═╝║╚╝║║║║╚╗╔╗╔╣╠╣║ {_RSTALL}")
    print(f"{_m_cl}╚╝{_b_cl}─{_m_cl}╚╝╚═╩═╩╝╚╩══╝╚═══╩══╝╚╝╚═╝╚╝╚══╩╝ {_RSTALL}")

def Fncls():
    if name == 'nt':
        _ = system('cls')
        print("ted")    
    else:
        _ = system('clear')

def handler(signum, frame):
    print("")
    FnExit(_N + _f_r + " Force Exit")



def FnExit(Msg=""):    
    if Msg != "":                
        print("")
        print(f'{Msg}')             
    sys.exit()

def checkDockerStatus():    
    client = None    
    try:        
        client = docker.DockerClient(base_url=DOCKER_URL,timeout = 5)
        client.ping()
        return True
    except docker.errors.DockerException as e:
        #print (f"ERROR MSG: {e}"        )
        return False
    finally:
        if client:
            client.close
def MainFn():
    Fncls()
    print("")
    logo()
    if checkDockerStatus() is False:
        FnErroMsg(f'{_f_ex_r}Unable to connect to the Docker daemon.{_RSTALL}')
        FnExit()
    ContainterFoundLst  = GetListofContainer()
    if ContainterFoundLst == []:
        FnErroMsg(f'{_f_r}None of the Atlassian software was found.{_RSTALL}')
        FnExit()
    ContainterFoundLst = FnDetectApplicationAndFetchData(ContainterFoundLst)        
    MainMenueLuncher(ContainterFoundLst)


def MainMenu(Containerlist):
    while True:            
        Fncls()
        print("")
        logo()
        PrintStatus(Containerlist)        
        print(f"\n{_RSTALL}{_f_w}type '{_D}{_f_w}Q{_N}{_f_w}' for quit{_RSTALL}")        
        commandlst = []
        for _ in Containerlist:
            commandlst.append(_)
            if len(Containerlist) == 1:
                _defValue = _
        
        if len(commandlst) == 1:
            UserInput = input(f'{_B}{_f_w}Press enter for Active {_f_y}{commandlst}{_f_w}:{_RSTALL}')                    
        elif len(commandlst) > 1:
            UserInput = input(f'{_B}{_f_w}Type Appliction name for Active It : {_f_y}{commandlst}{_f_w}:{_RSTALL}')            
        commandlst.append('q')

        if len(Containerlist)== 1:
            if UserInput.strip() == '':
                UserInput = _defValue
        if UserInput.lower().strip() in commandlst:
            return UserInput
        else:            
            print(f'\n{_f_r}Value [ {_f_w}{UserInput}{_f_r} ] Not Valid{_RSTALL}')
            input("Press enter to continue ...")

def MainMenueLuncher(Containerlist):
    UserInput = MainMenu(Containerlist)
    if UserInput == 'q':
        FnExit()
    else:        
        ActiveSrcLuncher(Appname=UserInput,ContainerDict=Containerlist)
    
def FnErroMsg(msg = ''):
    print("")
    print(f'{_f_ex_w}This Atlassian software activation system is only compatible with the {_f_ex_r}atlassoft.ir{_f_ex_w} installation and setup method.{_RSTALL}')
    if msg.strip() != '':        
        print("")
        print(f"{msg}{_RSTALL}")

def ActiveSrc(Appname:str,ContainerDict:dict):
    """
    Helping the user to get the activation code.
    Args:
        Appname: Appliction Name
        ContainerDict : Dict of container
    """
    while True:
        Fncls()
        logo()
        ContainerDetail = ContainerDict[Appname]
        ExtIp = GetExternalIp()
        if ExtIp == None:
            Msg1 = f"{_B}{_f_w}\n1- Open a browser and enter server {_f_b}IP Adreess{_f_w} with port [ {_f_b}{ContainerDetail['port']}{_f_w} ] :{_RSTALL}\n" 
            UrlStr = f'http://<IP>:{ContainerDetail["port"]}'
        else:
            Msg1 = f"{_B}{_f_w}\n1- Open a browser and enter the following address:{_RSTALL}\n"         
            UrlStr = f'http://{ExtIp}:{ContainerDetail["port"]}'
        msg_if  = f''
        Msg2 = f"{_B}{_f_w}\n2- Enter the requested information, When asked for license{_RSTALL}"
        Msg3 = f"{_B}{_f_w}3- {_f_y}Server ID{_f_w} is shown at License request step on license key Page{_RSTALL}"
        Msg4 = f'{_B}{_f_w}4- The server ID has a structure similar to ( {_f_b}XXXX-XXXX-XXXX-XXXX{_f_w} ).{_RSTALL}'
        Msg5 = f'{_B}{_f_w}5- paste or type it.{_RSTALL}\n'
        print (Msg1)
        BorderIt(UrlStr,TextColor=_f_ex_y,BorderColor=_f_b)
        print (Msg2)
        print (Msg3)
        print (Msg4)
        print (Msg5)
        ServerIDInput = input(f'{_B}{_f_w}Enter Server ID: {_b_y}{_f_bl}')
        if Validate_ServerID(ServerIDInput):            
            return ServerIDInput
        else:
            print(f'\n{_RSTALL}{_B}{_f_r}Entered value does not match the format.{_RSTALL}')
            input("Press enter to continue ...")

def ActiveSrcLuncher(Appname:str,ContainerDict:dict):
    ValidServerID = ActiveSrc(Appname=Appname,ContainerDict=ContainerDict)
    if Appname == 'jira':
        print("Run Fun Anf Get Lic type")
    else:
        print("OTHER")

def GetJiraLicMode():
    MenuDict = {
        "jira":"JIRA Software",
        "jsm" : "JIRA Service Management",
        "jc" :"JIRA Core",
        "jsd":"JIRA Service Desk"
    }

    while True:
        print(f"\n{_RSTALL}{_f_w}type '{_D}{_f_w}Q{_N}{_f_w}' for quit{_RSTALL}")        
        menuNumber = 1
        for _ in MenuDict:
            print(f'{menuNumber}- ')

        

def GetExternalIp()->str:
    try:    
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))  # Google's public DNS server
            return f"{s.getsockname()[0]}"
    except Exception as e:
        return None
    
def GetListofContainer()-> dict:
    containerNames = ['jira','bamboo','bitbucket','confluence','fisheye']
    ContainerDict = []
    client = None
    try:
        client = docker.DockerClient(base_url=DOCKER_URL)
        containers = client.containers.list()
        for container in containers:            
            if container.name.lower() in containerNames:                            
                _ports = FerchContainrerPort(container.ports)
                ContainerDict.append({
                    "ID": container.short_id,
                    "Name": container.name,                
                    "Status": container.status,                    
                    "ports" : _ports
                })
        return ContainerDict  
    except docker.errors.APIError as e:
        print(f"Error in Get List of container: {e}")
        return None
    finally:
        if client:
            client.close()

def FerchContainrerPort(ContainerPort:dict)-> list:
    portlist = []
    for _ in ContainerPort:
        _portDict = ContainerPort[_] 
        for _portNo in _portDict:
            if _portNo["HostIp"] == '0.0.0.0':
                portlist.append({_:_portNo["HostPort"]})
    return portlist            

def FnDetectApplicationAndFetchData(ContainterFoundedList):
    AppDict = {}
    for _ in ContainterFoundedList:
        if _['Name'] == 'jira':                        
            AllPorts = _['ports']
            ExosePort = FnGetExposePort('8080/tcp',AllPorts)
            MYcommand = '/opt/atlassian/jira/bin/version.sh'
            rst = FnExecuteCommand('jira',MYcommand)
            if rst[0] == 0:                
                JiraVersion = None
                for byte_data in rst[1].splitlines():
                    _line = byte_data.decode('utf-8')                   
                    index = _line.find('Version')
                    if index != -1:                        
                        lineLst = _line.split(':')
                        if JiraVersion == None:
                            JiraVersion = lineLst[1].strip()
                            continue
                    index = _line.find('Server version:')
                    if index != -1:
                        lineLst = _line.split(':')
                        TomcatVersion = lineLst[1].strip()
                        continue
                    index = _line.find('JVM Version:')
                    if index != -1:
                        lineLst = _line.split(':')
                        Java_Version = lineLst[1].strip()
                        continue


            #AppDict["jira"] = {'version':JiraVersion}            
            AppDict["jira"] = {}
            AppDict["jira"]["port"] = ExosePort
            AppDict["jira"]["ID"]= _["ID"]
            AppDict["jira"]["Status"]= _["Status"]
            AppDict["jira"]["version"] = JiraVersion
            AppDict["jira"]["Server_version"] = TomcatVersion
            AppDict["jira"]["Java_Version"] = Java_Version

        elif _['Name'] == 'confluence':
            print('confluence')
            
        return AppDict           


def FnGetExposePort(InternalPort,AllPorts):    
    for _ports in AllPorts:
        try:
            ports = _ports[InternalPort]
            return ports
        except:
            return None

def FnExecuteCommand(ContainerName,CommandStr):
    client = docker.from_env()
    try:
        container = client.containers.get(ContainerName)
        exit_code, output = container.exec_run(CommandStr)
        return exit_code,output
    except docker.errors.NotFound:
        FnErroMsg(f"Container '{ContainerName}' not found.")        
    except Exception as e:
        FnErroMsg(f"An error occurred: {_f_y}{e}")
    print()


def PrintStatus(Containerlist):
    """
    Get list Of Containter and Print It
    """
    NameStr = _b_w + _f_bl + Fn_String(originalString="Name",target_length=15,Aligment="left") + _RSTALL
    IdStr = _b_b + _f_w + Fn_String(originalString="ID",target_length=15,Aligment="left") + _RSTALL
    StatusStr = _b_b + _f_w + Fn_String(originalString="Status",target_length=10,Aligment="left") + _RSTALL
    AppStr = _b_b + _f_w + Fn_String(originalString="Application Server",target_length=24,Aligment="left") + _RSTALL
    JavaStr = _b_b + _f_w + Fn_String(originalString="JAVA Version",target_length=24,Aligment="left") + _RSTALL
    VerStr = _b_w + _f_bl + Fn_String(originalString="Version",target_length=24,Aligment="left") + _RSTALL

    print("")
    print(f'{NameStr} {VerStr} {IdStr} {StatusStr} {AppStr} {JavaStr}')
    print("")
    for _ in Containerlist:        
        _AppNameStr = f'{_f_ex_w}{Fn_String(originalString=_,target_length=15,Aligment="left")}'
        _verStr = f'{_f_ex_y}{Fn_String(originalString=Containerlist[_]["version"],target_length=24,Aligment="left")}'
        _IDStr = f'{_f_ex_w}{Fn_String(originalString=Containerlist[_]["ID"],target_length=15,Aligment="left")}'
        _StatusStr = f'{_f_ex_g}{Fn_String(originalString=Containerlist[_]["Status"],target_length=10,Aligment="left")}'
        _AppserverStr = f'{_f_ex_w}{Fn_String(originalString=Containerlist[_]["Server_version"],target_length=24,Aligment="left")}'
        _JavaStr = f'{_f_ex_w}{Fn_String(originalString=Containerlist[_]["Java_Version"],target_length=24,Aligment="left")}'
        print(f'{_AppNameStr} {_verStr} {_IDStr} {_StatusStr} {_AppserverStr} {_JavaStr}')



def Fn_String(originalString: str, target_length: int, padding_char: str = " ",Aligment = "center") -> str:
    if len(originalString) >= target_length:
        return originalString         
    total_padding = target_length - len(originalString)
    if Aligment not in ['center','left','right']:
        Aligment = 'left'
    if Aligment.lower() == 'center':        
        left_padding = total_padding // 2
        right_padding = total_padding - left_padding
        _str =  padding_char * left_padding + originalString + padding_char * right_padding
    elif Aligment.lower() == 'left':
        total_padding = total_padding - 1
        _str = padding_char + originalString + padding_char * total_padding
    elif Aligment.lower() == 'right':
        total_padding = total_padding - 1
        _str = padding_char * total_padding + originalString + padding_char
    return _str

def BorderIt(Text:str,BorderColor = '',TextColor = '', WidthBorder = 100):
    """ Create a Border in Text
    Args:
        Text (str): Input text
        BorderColor (str, optional): Border Color_. Defaults to 'WHITE'.
        TextColor (str, optional): TextColor. Defaults to 'WHITE'.
        WidthBorder (int, optional): Width of Box. Defaults to 100.
    """
    if TextColor == '':
        TextColor = _f_w
    if BorderColor == '':
        BorderColor = _f_w

    LenStr = len(Text) + 2
    if LenStr > WidthBorder:
        LenStr = WidthBorder         
    RowLine = '─' * LenStr
    Upline = BorderColor + f'┌{RowLine}┐' + _RSTALL
    Dwonline = BorderColor + f'└{RowLine}┘' + _RSTALL
    ClmnChar = f'{BorderColor}│{_RSTALL}'
    lines = wrap_text(text=Text,max_width=WidthBorder - 1)
    print(Upline)
    for line in lines:
        if LenStr == WidthBorder:            
            a = WidthBorder - len(line) - 1
            space_al = ' ' * a
        else:
            space_al = ' '    
        print(f'{ClmnChar} {TextColor}{line}{space_al}{ClmnChar}')
    print(Dwonline)


def wrap_text(text, max_width=100):
    """
    Wraps the given text to a specified maximum width.

    Args:
        text: The input text to be wrapped.
        max_width: The maximum width of each line.

    Returns:
        A list of lines, where each line has a maximum width of max_width.
    """

    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 > max_width:  # Add 1 for the space
            lines.append(current_line.strip())
            current_line = word + " "
        else:
            current_line += word + " "
    
    if current_line.strip():
        lines.append(current_line.strip())
    return lines

def Validate_ServerID(input_string):
    """
    Validates if the input string matches the format "XXXX-XXXX-XXXX-XXXX"   
    Args:
        input_string: The string to be validated.
    Returns:
        True if the input string matches the format, False otherwise.
    """
    pattern = r"^[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$"
    return bool(re.match(pattern, input_string))

signal.signal(signal.SIGINT, handler)

if __name__ == '__main__':                
    if len(sys.argv) == 1:
        MainFn()
