#Bubble sort of numeric data without using 3rd variable

#Try it online https://code.sololearn.com/c6uI3ZlD5Nj4

instr=list("57335527388546344")
print("Input Str",instr)
c=0
while c<len(instr)-1:
 n=0
 while n<len(instr)-1:
  #print(instr[n],instr[n+1])
  if int(instr[n])>int(instr[n+1]):
   instr[n]=int(instr[n])+int(instr[n+1])
   instr[n+1]=int(instr[n])-int(instr[n+1])
   instr[n]=int(instr[n])-int(instr[n+1])
   #print("swapped")
   #print(instr)
  n+=1
 c+=1
print("Output Str",instr)

#Bubble sort with using 3rd variable#
instr=list("57335gdueysf66473a")
print("Input Str",instr)
c=0
while c<len(instr)-1:
 n=0
 while n<len(instr)-1:
  #print(instr[n],instr[n+1])
  if instr[n]>instr[n+1]:
   i=instr[n]
   instr[n]=instr[n+1]
   instr[n+1]=i
   #print("swapped")
   #print(instr)
  n+=1
 c+=1  
print("Output Str",str(instr))
