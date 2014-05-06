'''
Created on May 5, 2014
This code return the IPTables firewall information
@author: srini
'''
import iptc

def getIPTablesInfo():
    table = iptc.Table(iptc.Table.FILTER)
    s = ""
    for chain in table.chains:
        s = s + "==============================================\n"
        s = s + "Chain " + str(chain.name) + "\n"
        for rule in chain.rules:
            s = s + "Rule" + " protocol:" + str(rule.protocol) + " source:" + str(rule.src) + " destination:" + str(rule.dst) + " in:" + str(rule.in_interface) + " out:" + str(rule.out_interface) + "\n"
            s = s + "Matches: "  
            for match in rule.matches:
                s = s + str(match.name) + ","
            s = s.strip(",") + "\n"
            s = s + "Target:" + str(rule.target.name) + "\n"
    return s
    
if __name__ == '__main__':
    print getIPTablesInfo()