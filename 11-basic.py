#Loop in python

cars = ["supra", "gtr", "formula1", "ferrari"]
for brand in cars:
 if(brand == "formula1"):
  continue
 print(brand)
 
 
 
cars = ["supra", "gtr", "formula1", "ferrari"]
for brand in cars:
 if(brand == "formula1"):
  break
 print(brand)
 
 car = range(5)
 for nth in car:
  print(nth)
  

name = ["jilian", "jacob", "malaria", "jonabels"]
age = [21,13,24,20]

for ngalan in name:
 for edad in age:
  print(ngalan,edad)
  
  
  i = 1
  while i <= 10:
   i += 1
   if i == 3:
    continue
   print(i)

#part 1
   