import re, os, sys
from termcolor import colored,cprint


if os.path.exists(sys.argv[1].replace(".xml", "")):
    pass
else:
    os.mkdir(f"{os.getcwd()}/{sys.argv[1].replace('.xml', '')}")

choise = input("Active Scan?> y/n ")
with open(sys.argv[1], "r") as file:
    trigger_print = False
    temp_list = []
    for line in file:
        line = line.strip()
        if 'addrtype="ipv4"' in line:
            ip = re.search('(?:<.* addr=")(\d*.\d*.\d*.\d*)(?:" .*="ipv4"/>)', line)
            temp_list.append(ip.group(1))
        if "<ports>" in line:
            trigger_print = True

        if trigger_print == True:
            port = re.search('(?:portid=)"(\\d*)"(?:>)', line)
            state = re.search('(?:state=")(\w*)(?:")', line)
            if port:
                if state != 'closed' and state != 'filtered':
                    temp_list.append(port.group(1))

        if "</ports>" in line:
            trigger_print = False
            command = f"nmap {temp_list[0]} -Pn -sC -sV --open -p"
            if len(temp_list) == 1:
                temp_list.clear()
                continue
            else:
                cprint(f"\n-----------------------------------------------\nIP: {temp_list[0]}", "red")
                command = f"nmap {temp_list[0]} -v -Pn --open -sC -sV -p"
                for i in range(1, len(temp_list)):
                    if "443" in temp_list[i]:
                        cprint(f"\t{temp_list[i]}   :   Open\nOpen in Browser: https://{temp_list[0]}:{temp_list[i]}/", "green")
                    else:
                        cprint(f"\t{temp_list[i]}   :   Open\nOpen in Browser: http://{temp_list[0]}:{temp_list[i]}/", "green")

                    command = command + temp_list[i] + ","
                    os.system(f"echo {temp_list[0]} >> {sys.argv[1].replace('.xml', '')}/{temp_list[i]}.txt")

                if choise == "y".lower():
                    cprint("\n----------Enumerating----------\n", "red")
                    print(f"Using the following command: {command[:len(command)-1]}\n")
                    os.system(command[:len(command)-1])
                    cprint("\n\n-------------------------Done----------------------\n\n", "red")
                else:
                    print(f"Use the following for nmap scan: {command[:len(command)-1]}\n")


            command = ""
            temp_list.clear()
        
