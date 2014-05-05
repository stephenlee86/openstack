'''
Created on May 4, 2014
This file has code that get information on the users, hosts and databases that are accessed in MySQL database
Can include other databases in future by providing wrapper apis  
@author: srini
'''
import MySQLdb, json

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
    return json.dumps(lidict)

if __name__ == '__main__':
    getUserHostDBDict("localhost","root", "a")