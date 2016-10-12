#! usr/bin/env python
# -*- coding:utf-8 -*-

def checkIP(ip):
    q = ip.split('.')
    print(q)
#    return len(q) == 4 and len(filter(lambda x: x >= 0 and x <= 255,map(int, filter(lambda x: x.isdigit(), q)))) == 4
    return (filter(lambda x: x >= 0 and x <= 255,map(int, filter(lambda x: x.isdigit(), q))))

if __name__=='__main__':
    ip = input()
    print(checkIP(ip))

