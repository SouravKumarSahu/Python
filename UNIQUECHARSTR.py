#Unique Characters From A String

#Try it online https://code.sololearn.com/czg43ejOGCr7

#When Input String is Sorted
instring="abbbccdefghhhijkllmmnnoopqrstuvxyzz"
inlength = len(instring) - 1
#print(inlength)
outstring = ""
for i in range(0,inlength):
 if instring[i] != instring[i+1]:
  outstring += instring[i]
  #print(outstring)
 if i == inlength:
  print(instring[i + 1])
print("instring = ",instring)
print("outstring = ",outstring)

#When String is not Sorted
instring = "ABBABBBBBDIIOEBAIDOBCOWGONSVOOWNBAZZZWDBSBaaaarrrrratataggeyvstwztaie16337265$$$#@&@&"
outstring = ""
for i in instring:
    flag = 0
    for j in outstring:
        if i == j:
            flag +=1
    if flag == 0:
        outstring += i
print("instring = ",instring)
print("outstring = ",outstring)

#Or simply use set
instring = "ABBABBBBBDIIOEBAIDOBCOWGONSVOOWNBAZZZWDBSBaaaarrrrratataggeyvstwztaie16337265$$$#@&@&"
outstring = "".join(str(c) for c in set(instring))
print("instring = ",instring)
print("outstring = ",outstring)
