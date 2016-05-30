import plistlib
pl = plistlib.readPlist("MtrResourcesKTEnSILE.plist")
a = pl["Root"]
b = a["SystemMapRoute"]
routeInfo = b["Route"]
#AEL = routeInfo["AEL"]
for key in routeInfo:
    for key1 in routeInfo[key]:
        value1 = routeInfo[key][key1]
        d1 = value1[1:len(value1)-1]
        num1 = d1.split(', ')[0]
        num2 = d1.split(', ')[1]
        s1 = int(num1)-2
        s2 = int(num2)
        modifiedStr = "{"+str(s1)+", "+str(s2)+"}"
        routeInfo[key][key1] = modifiedStr
#print routeInfo
b["Route"] = routeInfo
plistlib.writePlist(pl,"modifiedRoute.plist")

#for c in b:
#    d = c["Point"]
#    d1 = d[1:len(d)-1]
#    num1 = d1.split(', ')[0]
#    num2 = d1.split(', ')[1]
#    s1 = int(num1)-6
#    s2 = int(num2)+16
#    modifiedStr = "{"+str(s1)+", "+str(s2)+"}"
#    c["Point"] = modifiedStr
#    print modifiedStr
#plistlib.writePlist(pl,"modified.plist")
