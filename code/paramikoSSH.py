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
    scp %s %s
    exit
    ''' %("currentLocationDirectory","remoteLocationDirectory"))
    result = stdout.read()
    stdout.close()
    stdin.close()
    ssh.close()
    return result

if __name__ == '__main__':
    execute_command("obelix.cs.umass.edu", "srxxx", "xxxxxxx", "ls -al")
    print login('obelix.cs.umass.edu','srxxx','xxxxxxx')