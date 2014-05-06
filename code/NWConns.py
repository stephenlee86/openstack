'''
Created on May 6, 2014
This code is used to monitor connections over the network.

Returns a list of dictionary which contains teh following - 
1) Total connection details
2) Total number of connections
3) Total active connections details
4) Total number of active connections
5) List of different status messages
 
Assumption - Needs sudo 

Extension - This can be easily extended to get additional information such as - 
CPU, memory, disks, network  
@author: srini
'''
import psutil

def getActiveConnections():
    dictli = {}
    results = psutil.net_connections()
    dictli["total connections"] = len(results)
    dictli["total results"] = results
    li = []; uni = []
    for result in results:
        if result[5]!="NONE":
            li.append(result)
        if result[5] not in uni:
            uni.append(result[5])
    dictli['active connections'] = len(li)
    dictli['active results'] = li
    dictli['all status'] = uni
    return dictli

if __name__ == '__main__':
    print getActiveConnections()
