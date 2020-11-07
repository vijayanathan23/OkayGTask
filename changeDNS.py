import json 
import os
inputFile = open('data.json',) 
data = json.load(inputFile) 
name = data["name"]
service = "service" #by default this script is for service.com as we are using the key for service.com
ttl = "1h"
Type = data["type"] #Eg: A(IPV4)/AAAA(IPV6)/CNAME
infos = data["data"]#Eg: IP/MX records

updateText = "server master.dns.server.service.com\n";
updateText = updateText+"debug yes\n";
updateText = updateText+"zone service.com.\n"
updateText = updateText+"update add "+name+" 1h "+Type+" "
for x in infos:
	updateText = updateText+x+" "

updateText = updateText+"\nshow\n"+"send"
f = open("nsupdate.txt", "a")
f.write(updateText)
#Using command line for nsupdate with reqd parametersfor updation
os.system('nsupdate -k Kservice.com.+008+17004.private -v nsupdate.txt')
#The Kservice private key is from dnssec...Using a command(Refer github's readme!)
f.close()
inputFile.close() 


#Done by vijayanathan
#referance 	http://agiletesting.blogspot.com/2012/03/dynamic-dns-updates-with-nsupdate-and.html
#and https://linuxhint.com/install_bind9_ubuntu/
#also, bind9 documentation
