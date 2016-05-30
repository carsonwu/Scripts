import plistlib
pl = plistlib.readPlist("MtrResourcesWIL.plist")
a = pl["Root"]
b = a["SystemMap"]
for c in b:
    d = c["Point"]
    d1 = d[1:len(d)-1]
    num1 = d1.split(', ')[0]
    num2 = d1.split(', ')[1]
    s1 = int(num1)-6
    s2 = int(num2)+16
    modifiedStr = "{"+str(s1)+", "+str(s2)+"}"
    c["Point"] = modifiedStr
    print modifiedStr
plistlib.writePlist(pl,"modified.plist")
