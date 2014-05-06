'''
Created on May 4, 2014
This file has code that get information on the users, hosts and databases that are accessed in MySQL database
Can include other databases in future by providing wrapper apis  
@author: srini
'''
import MySQLdb, socket

def getUserHostDBDict(ip,uname,pword):
    db = MySQLdb.connect(host=ip, user=uname,passwd=pword, db="mysql")
    cur = db.cursor() 
    cur.execute("SELECT User, Host, Db FROM db;")
    lidict = []
    for row in cur.fetchall() :
        dict = {}
        dict['user'] = row[0]
        dict['host'] = row[1]
        dict['db'] = row[2]
        lidict.append(dict)
    return lidict

def getDBScan(ip,uname,pword):
    results = getUserHostDBDict(ip, uname, pword)
    names = []
    names.append(ip)
    names.append(socket.gethostbyname(ip))
    ipv4_addr = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1] 
    names.append(ipv4_addr)
    names.append(socket.gethostbyaddr(ipv4_addr)[0])
    names = list(set(names))
    dictli = {}; s = ""
    for result in results:
        s = s + "," + str(result["host"])
    li = s.strip(",").split(",")
    for name in names:
        li = [x for x in li if x != name]
    dictli['hosts'] = list(set(li))
    if len(li)==0:
        dictli["code"] = "Green"
    elif len(li)<=3:
        dictli["code"] = "Amber"
    else:
        dictli["code"] = "Red"
    return dictli
    
if __name__ == '__main__':
    print getUserHostDBDict("localhost","root", "a")
    print getDBScan("localhost","root", "a")