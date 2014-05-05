'''
Created on Apr 7, 2014
his file deals with nmap command related queries to get the following - 
1) To find open ports
2) Topology information to get the connections between hosts on a network
3) Allowed ip protocols
4) General firewall information  
@author: srini
'''
import subprocess, json, sys
import common

def commandResponse(nmapCommand,ipAddress):
    return subprocess.check_output(nmapCommand + ipAddress, shell=True).split("\n")

def formListDict(info,keys):
    liDict = []
    for ele in info:
        items = ele.split()
        dictimp = {}
        for i in range(len(keys)):
            dictimp[keys[i]] = items[i]
        liDict.append(dictimp)
    return json.dumps(liDict)

def openPorts(ipAddress):
    return formListDict(common.getInterTagInfo(commandResponse("nmap --top-ports 20 ", ipAddress), "PORT    STATE SERVICE", "MAC Address:"))

def topologyInfo(ipAddress):
    return formListDict(common.getInterTagInfo(commandResponse("nmap -sn --traceroute ", ipAddress), "HOP RTT     ADDRESS", "Nmap done:"))

def allowedIPProtocols(ipAddress):
    return formListDict(common.getInterTagInfo(commandResponse("nmap -sO ", ipAddress), "PROTOCOL STATE SERVICE", "MAC Address:"))

def firewallInfo(ipAddress):
    return formListDict(common.getInterTagInfo(commandResponse("nmap ", ipAddress), "PORT    STATE SERVICE", "Nmap done:"))

if __name__ == '__main__':
    ipAddress = sys.argv[0]
    print firewallInfo(ipAddress)
    print allowedIPProtocols(ipAddress)
    print openPorts(ipAddress)
    print topologyInfo(ipAddress)
    