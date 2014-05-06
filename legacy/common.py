'''
Created on May 4, 2014
This file is used to call functions that are used to parse and retrieve the results of a query
@author: srini
'''

def index_containing_substring(the_list, substring):
    for i, s in enumerate(the_list):
        if substring in s:
            return i
    return -1

def getInterTagInfo(result,startTag,endTag):
    keys = startTag.split()
    info = result[result.index(startTag)+1:index_containing_substring(result,endTag)]
    info.remove("")
    return info,keys

def getInterTagInfoWKey(result):
    li = result.split("\n")
    newli = []; keys = []; finli = []
    for ele in li:
        if "|" in ele:
            newli.append(ele)
    first = True
    for ele in newli:
        inli = ele.split("|")
        if first:
            keys.append(inli[1].strip())
            keys.append(inli[2].strip())
            keys.append(inli[3].strip())
            first = False
        else:
            dict = {}
            for key in keys:
                dict[key] = inli[keys.index(key)+1].strip()
            finli.append(dict)
    return finli