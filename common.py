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