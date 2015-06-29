import time
import sys
import itertools

starttime = time.time()

container = []

# Generating triangular numbers

t = lambda x : (x * (x + 1) / 2)
tri = {}

for i in range(45,141):
    tri[i] = t(i)

print "Created Triangle numbers", len(tri)

container.append(tri)

# Generating Square numbers

s = lambda x: (x * x)
sqr = {}

for i in range(32,100):
    sqr[i] = s(i)

print "Created Square numbers", len(sqr)
container.append(sqr)

# Generating Pentagonal Numbers

pe = lambda x: (x * (3 * x - 1)) / 2
pent = {}

for i in range(26, 82):
    pent[i] = pe(i)

print "Created Pentagonal numbers", len(pent)
container.append(pent)

# Generating Hexagonal Numbers

he = lambda x: x * (2 * x - 1)
hexa = {}

for i in range(23,71):
    hexa[i] = he(i)

print "Created Hexagonal numbers", len(hexa)
container.append(hexa)


# Generating Heptagonal Numbers
hep = lambda x : (x * (5 * x - 3)) / 2
hept = {}

for i in range(21,64):
    hept[i] = hep(i)

print "Created Heptagonal Numbers", len(hept)
container.append(hept)

# Generating Octagonal Numbers
oc = lambda x: (x * (3 * x - 2))
octa = {}

for i in range(19,59):
    octa[i] = oc(i)

print "Created Octagonal Numbers", len(octa)
container.append(octa)

print "\n\n"
# all the numbers are ready . Lets create a list with all the numbers
allNums = []

allNums = tri.values() + sqr.values() + pent.values() + hexa.values() + hept.values() + octa.values()
allNums = list(set(allNums))
#print allNums


commonDict = {}

# Now, the logic to find the cyclic numbers
la = len(allNums)
removeList = []
for i in range(la):
    num1 = allNums[i]
    num1_lt = num1 % 100
    commonlist = []
    for j in range(la):
        num2 = allNums[j]
        num2_ft = num2 / 100
        if num1_lt == num2_ft:
            commonlist.append(num2)
          
    if len(commonlist) == 0:
        removeList.append(num1)
    else:
        commonDict[num1] = commonlist


allNums = [x for x in allNums if x not in removeList]
la = len(allNums)


print "Starting here"

def getFlags(a,b,c,d,e,f):

    ref = {}
    ref[0] = "T"
    ref[1] = "S"
    ref[2] = "P"
    ref[3] = "H"
    ref[4] = "He"
    ref[5] = "O"

    result = {}
    for i in range(len(container)):
        eachDict = container[i]

        if a in eachDict.values():
            if a not in result:
                temp = []
                temp.append(ref[i])
                result[a] = temp
            else:
                temp = result[a]
                temp.append(ref[i])
                result[a] = temp

        if b in eachDict.values():
            if b not in result:
                temp = []
                temp.append(ref[i])
                result[b] = temp
            else:
                temp = result[b]
                temp.append(ref[i])
                result[b] = temp

        if c in eachDict.values():
            if c not in result:
                temp = []
                temp.append(ref[i])
                result[c] = temp
            else:
                temp = result[c]
                temp.append(ref[i])
                result[c] = temp

        if d in eachDict.values():
            if d not in result:
                temp = []
                temp.append(ref[i])
                result[d] = temp
            else:
                temp = result[d]
                temp.append(ref[i])
                result[d] = temp


        if e in eachDict.values():
            if e not in result:
                temp = []
                temp.append(ref[i])
                result[e] = temp
            else:
                temp = result[e]
                temp.append(ref[i])
                result[e] = temp

        if f in eachDict.values():
            if f not in result:
                temp = []
                temp.append(ref[i])
                result[f] = temp
            else:
                temp = result[f]
                temp.append(ref[i])
                result[f] = temp

    if len(result.keys()) == 6:

        testList = itertools.chain (result[a] , result[b] , result[c] , result[d] , result[e], result[f])
        li = list(testList)
        if "T" in li and "S" in li and "P" in li and "H" in li and "He" in li and "O" in li:
            #print a,b,c,d,e,f, " : " , li
            print result
            #print "\n"


for a in allNums:
    if a not in commonDict:
        continue
    for b in commonDict[a]:
        if b not in commonDict:
            continue
        for c in commonDict[b]:
            if c not in commonDict:
                continue
            for d in commonDict[c]:
                if d not in commonDict:
                    continue
                for e in commonDict[d]:
                    if e not in commonDict:
                        continue
                    for f in commonDict[e]:
                        if a / 100 == f % 100:
                            #print a,b,c,d,e,f
                            getFlags(a,b,c,d,e,f)
                            


endtime = time.time()
print "Executed in " , endtime - starttime, "Seconds"
