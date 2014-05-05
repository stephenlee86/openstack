"""
This file has code that get information on the users, hosts and databases that are accessed in MySQL database
Can include other databases in future by providing wrapper apis  
"""
import paramiko
import common

def execute_command(host, user, key, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, key_filename=key)
    stdin, stdout, stderr = client.exec_command(command)
    print "stderr: ", stderr.readlines()
    print "pwd: ", stdout.readlines()
    return stderr, stdout

def login(host, user, passw, dbcred):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passw)
    channel = ssh.invoke_shell()
    stdin = channel.makefile('wb')
    stdout = channel.makefile('rb')
    stdin.write('''
    mysql -u%s -p%s
    %s
    exit
    exit
    ''' %(dbcred['user'],dbcred['password'],dbcred['command']))
    result = common.getInterTagInfoWKey(stdout.read())
    #result = common.getInterTagInfo(result, "mysql> " + dbcred['command'], "rows in set")
    stdout.close()
    stdin.close()
    ssh.close()
    return result

if __name__ == '__main__':
    dbcred = {}
    dbcred['user'] = "root"; dbcred['password'] = "a"; dbcred['command'] = "SELECT User, Host,Db FROM mysql.db;";
    print login('obelix.cs.umass.edu','srini','Aman@1234',dbcred)
    #command = "mysql " + "-u" + dbcred['user'] + " -p" + dbcred['password'] + " -e " + "\"" + dbcred['command'] + "\""
    #execute_command("obelix.cs.umass.edu", "srini", "Aman@1234", dbcred) 