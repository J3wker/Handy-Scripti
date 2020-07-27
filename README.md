# Handy-Scripti
handy scripts i write during PT and i think would help others

# masscanner-beautifier.py
Date: 26/07/2020

A script to output your mascan results nicely from an XML format  
Organize them in a folder - and create txt files for each ports to see which IPs  
are open on which ports - for example:  

22.txt  
    127.0.0.1  
    192.168.1.1  

Also - Active mod will scan with -sC -sV the ports that masscan reported as open  
Passive will only do the stuff i mentioned above   

# nmap-beautifer.py #
Date: 27/07/2020

A script to output your nmap.xml results nicely from an XML format  
Organize them in a folder - and create txt files for each ports to see which IPs  

Also Gives you the option to scan them using -sC -sV flags for further information

are open on which ports - for example:  

22.txt  
127.0.0.1  
192.168.1.1  

Also - Active mod will scan with -sC -sV the ports that masscan reported as open  
Passive will only do the stuff i mentioned above   

For BEST use: nmap -Pn -p- -T4 *--open* -oX example.xml
