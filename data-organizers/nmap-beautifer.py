import re, os, sys


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
            if port:
                temp_list.append(port.group(1))

        if "</ports>" in line:
            trigger_print = False
            print(f"\n-----IP: {temp_list[0]}-----\n")
            command = f"nmap {temp_list[0]} -Pn -sC -sV --open -p"
            for i in range(1,len(temp_list)):
                command = command + f"{temp_list[i]},"
                if "443" in temp_list[i]:
                    print(f"Open in Browser:\n https://{temp_list[0]}:{temp_list[i]}/\n")
                else:
                    print(f"Open in Browser:\n http://{temp_list[0]}:{temp_list[i]}/\n")

                os.system(f"echo {temp_list[0]} >> {sys.argv[1].replace('.xml', '')}/{temp_list[i]}.txt")
                if choise == "y".lower():
                    if command.endswith(","):
                        command = command[:len(command)-1]

                    os.system(command)
            print("\n-------------------------Done---------------------------\n")

            temp_list.clear()
        