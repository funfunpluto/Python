#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))



print(sum([1 for x in apple if (x >= s - a and x <= t -a)]))

print(sum([1 for x in orange if (x >= s - b and x <= t -b)]))    

                                                                                                                                                                                                               
