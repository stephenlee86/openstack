import os
import novaclient.v1_1.client as nvclient

def get_keystone_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d

def get_nova_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

def nova_security_group_allowed_ports():
    creds = get_nova_creds()
    nova = nvclient.Client(**creds)

    open_ports= {}

    for group in nova.security_groups.list():
        for rule in group.rules:
            #print rule
            #{u'from_port': 22, u'group': {}, u'ip_protocol': u'tcp', u'to_port': 22, u'parent_group_id': 1, u'ip_range': {u'cidr': u'0.0.0.0/0'}, u'id': 1}
            if open_ports.has_key(group.id):
                open_ports[group.id].append(rule['from_port'])
                #print open_ports[group.id]
            else:
                open_ports[group.id] = [rule['from_port']]
    print open_ports
    return open_ports

if __name__ == "__main__":
     nova_security_group_allowed_ports()

