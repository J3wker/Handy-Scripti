import sys
import re
import os
from termcolor import cprint
ips = []
final_list = []
data = open(sys.argv[1], "r")
data_read = data.read()
# (?:portid=")(.*)(?:">)

"""
Author: Omri Baso
Date: 26/07/2020

A script to output your mascan results nicely from an XML format
Organize them in a folder - and create txt files for each ports to see which IPs
are open on which ports - for example:

22.txt
    127.0.0.1
    192.168.1.1

Also - Active mod will scan with -sC -sV the ports that masscan reported as open
Passive will only do the stuff i mentioned above 
"""

def find_ips():
	ip_list = re.findall('(?:<address addr=")(.*)(?:\" add)', data_read)
	for ip  in ip_list:
		if ip not in ips:
			ips.append(ip)


def main():
	if os.path.exists(sys.argv[1].replace(".xml", "")):
		pass
	else:
		os.mkdir(f"{os.getcwd()}/{sys.argv[1].replace('.xml', '')}")

	find_ips()
	choise = input("Active scan with nmap on results? y/n ")
	print(ips)
	for ip in ips:
		temp_list = []
		temp_list.append(ip)
		with open(sys.argv[1], "r") as file:
			for line in file:
				line = line.strip()
				if ip in line:
					port = re.search('(?:portid=")(.*)(?:">)', line)
					temp_list.append(port.group(1))

			cprint(f"\n-----------------------------------------------\nIP: {temp_list[0]}", "red")
			command = f"nmap {temp_list[0]} -v -Pn -sC -sV -p"
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
                
                

			


if __name__ == "__main__":		
	main()
