import paramiko

def execute_command(host, user, key, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, key_filename=key)
    stdin, stdout, stderr = client.exec_command(command)
    print "stderr: ", stderr.readlines()
    print "pwd: ", stdout.readlines()
    return stderr, stdout

def login(host, user, passw):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passw)
    channel = ssh.invoke_shell()
    stdin = channel.makefile('wb')
    stdout = channel.makefile('rb')
    stdin.write('''
    rmdir %s
    exit
    ''' %("df"))
    result = stdout.read()
    stdout.close()
    stdin.close()
    ssh.close()
    return result
"""
sshpass -p 'Aman@1234' ssh srini@obelix61
mysql -uroot -pa -e \"show databases;\"
"""
if __name__ == '__main__':
    #execute_command("obelix.cs.umass.edu", "srini", "Aman@1234", "ls")
    print login('obelix.cs.umass.edu','srini','Aman@1234')