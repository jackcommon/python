import functools
import teocommon_operation
import os

def stringhandle(s):
    alist = list(map(lambda x: ord(x)-64, s))
    result = functools.reduce(lambda x, y: x+y, alist)
    return result

if os.access('names.txt', os.R_OK):
    with open('names.txt','r',-1,encoding='utf-8') as rf:
        lines = rf.readlines()
        for i, line in enumerate(lines):
            line = line.replace('\n','')
            alist = line.split(',')
blist = sorted(list(map(lambda x: x.strip('"'), alist)))

result =0
for i, value in enumerate(blist):
    result += (i+1) * stringhandle(value)

print(result)
