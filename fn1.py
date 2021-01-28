fh = open('mbox-short.txt')
s = 0
for line in fh:
    di = dict()
for line in handle :
    line = line.rstrip()
    if line.startswith("From: ") :
        line = line.rstrip()
        str = line
        wds = str[str.find(':')+2:]
        di[wds] = di.get(wds, 0) + 1
largest = -1
theword = None
for k, v in di.items() :
    if v > largest :
        theword = k
        largest = v
print (theword, largest)