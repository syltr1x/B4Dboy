import subprocess as sp

def detect_os():
    os = str(sp.check_output('cat /etc/os-release', shell=True))[2:][:-1].split('\\n')
    os = os[2].split("=")[1]
    return os

def detect_cli():
    try: 
        sp.call('netcat', shell=True)
        val = "netcat"
    except:
        val = 0
    try:
        sp.call('ncat', shell=True)
        val = "ncat"
    except:
        val = 0
    return val

def install_cli(os=""):
    if os == "arch":
        sp.call('sudo pacman -S nmap', shell=True)
    elif os == "debian" or os == "parrot" or os == "kali" or os == "ubuntu":
        sp.call('sudo apt install nmap', shell=True)
    else:
        print("Error: Netcat Cli not found, please install manually")

def exec_cli(args=[""]):
    print(f"netcat", ' '.join([i for i in args]))

exec_cli(args=["-lvp", "9080", "-e /bin/bash"])

#cli = detect_cli()
#if cli != 0: print(f"Client Found:{cli}")
#else: install_cli(detect_os())