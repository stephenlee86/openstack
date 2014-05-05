'''
Created on May 5, 2014
This code is used to return a json object which is essentially a list of dictionaries 
containing protocol, port, state, name of the service for a given ipAddress

Assumption - 
Sudo access
NMAP installed 
@author: srini
'''
import nmap
import json

def getPortInformation(ipAddress):
    nm = nmap.PortScanner()
    nm.scan(ipAddress)
    dictli = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            lport.sort()
            for port in lport:
                dict = {}
                dict['protocol'] = proto
                dict['port'] = port
                dict['state'] = nm[host][proto][port]['state']
                dict['name'] = nm[host][proto][port]['name']
                dictli.append(dict)
    return json.dumps(dictli)

if __name__ == '__main__':
    getPortInformation("localhost")