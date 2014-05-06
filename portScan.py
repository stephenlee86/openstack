'''
Created on May 5, 2014
This code is used to return a json object which is essentially a list of dictionaries 
containing protocol, port, state, name of the service for a given ipAddress

Assumption - 
Sudo access
NMAP installed 
@author: srini
'''
import nmap, sys

def getPortInformation(ipAddress):
    nm = nmap.PortScanner()
    nm.scan(ipAddress)
    dictli = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            lport.sort()
            for port in lport:
                dicti = {}
                try:
                    dicti['protocol'] = proto
                    dicti['port'] = port
                    dicti['state'] = nm[host][proto][port].get('state','NA')
                    dicti['name'] = nm[host][proto][port].get('name','NA')
                    dictli.append(dicti)
                except:
                    continue
    return dictli

def getPortScan(ipAddress):
    result = getPortInformation(ipAddress)
    dictli = {}
    if len(result)<=2:
        dictli["code"] = "Green"
    elif len(result)<=4:
        dictli["code"] = "Amber"
    else:
        dictli["code"] = "Red"
    s = ""
    for ele in result:
        if str(ele['state']).lower()=="open":
            s = s + "," + str(ele['port'])
    dictli['openPorts'] = s
    return dictli

if __name__ == '__main__':
    ipAddress = sys.argv[0]
    print getPortInformation(ipAddress)
    print getPortScan(ipAddress)