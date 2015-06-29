__author__ = 'user'

import time
import sys

starttime = time.time()

nc = {}
cs = {}
for num in range(5, 10000):
    cube = num * num * num
    nc[num] = cube
    sorted_num = ''.join(sorted(str(cube)))
    cs[num] = sorted_num



for key, value in cs.iteritems():
    li = []
    li.append(key)
    for k, v in cs.iteritems():
        if k != key and value == v:
            li.append(k)

    if len(li) == 5:
        print key, li





endtime = time.time() - starttime





print "Program ran in " , endtime, "Seconds"
