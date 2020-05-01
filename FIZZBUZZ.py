lim=106
loop=9
#FizzBuzz Interview test
if loop == 1:
 #Basic
 for i in range(1,lim):
  if i % 3 == 0:
   print("Fizz")
  elif i % 5 == 0:
   print("Buzz")
  else:
   print(i)
elif loop == 2:
 #Better
 for i in range(1,lim):
  if i % 3 == 0:
   print("Fizz")
  if i % 5 == 0:
   print("Buzz")
  if (i%3!=0) and (i%5!=0):
   print(i)
elif loop == 3:
 #Better
 for i in range(1,lim):
  if i % 3 == 0:
   print("Fizz")
  if i % 5 == 0:
   print("Buzz")
  if (i%3==0) and (i%5==0):
   print("FizzBuzz")
  if (i%3!=0) and (i%5!=0):
   print(i)
elif loop == 4:
 #Better
 for i in range(1,lim):
  if (i%3==0) and (i%5!=0):
   print("Fizz")
  if (i%3!=0) and (i%5==0):
   print("Buzz")
  if (i%3==0) and (i%5==0):
   print("FizzBuzz")
  if (i%3!=0) and (i%5!=0):
   print(i)
elif loop == 5:
 #Better
 for i in range(1,lim):
  if (i%3==0) and (i%5==0):
   print("FizzBuzz")
  elif (i%3==0):
   print("Fizz")
  elif (i%5==0):
   print("Buzz") 
  else:
   print(i)
elif loop == 6:
 #Better
 for i in range(1,lim):
  strng=""
  if (i%3==0):
   strng=strng + "Fizz"
  if (i%5==0):
   strng=strng + "Buzz"
  if (strng==""):
   strng=i
  print(strng)
elif loop == 7:
 #Better
 for i in range(1,lim):
  strng=""
  if (i%3==0):
   strng += "Fizz"
  if (i%5==0):
   strng += "Buzz"
  if (strng==""):
   strng=i
  print(strng)
elif loop == 8:
 #Best Yet
 for i in range(1,lim):
  strng=""
  if (i%3==0):
   strng += "Fizz"
  if (i%5==0):
   strng += "Buzz"
  if (i%7==0):
   strng += "Fuzz"
  if (strng==""):
   strng=i
  print(strng) 
elif loop == 9:
 #Interesting
 for i in range(1,lim):
  strng=""
  if (i%1==0):
   strng += "Ooz"
  if (i%3==0):
   strng += "Fizz"
  if (i%5==0):
   strng += "Buzz"
  if (i%7==0):
   strng += "Fuzz"
  if (strng==""):
   strng=i
  print(strng) 
