def bubbleSort(unordered):
  ordered = unordered
  n= len(unordered)
  
  for i in range(n - 1):
    swap = False
    for j in range(n - 1):
      if ordered[j]>ordered[j + 1]:
        ourSwap = ordered[j]
        ordered[j] = ordered[j + 1]
        ordered[j + 1] = ourSwap
        
        swap = True
    
    if not swap:
      break
  return ordered
  
import random

array = []

for i in range (10):
  array.append(random.randint(1 , 50))
  
print array

array2 = bubbleSort(array)
print array2

inf = 0
sup = 10
buscar = False

X = int(input("ingresa numero"))

while ( not(buscar) and inf <= sup):
  
  mitad = int((inf + sup)/2)
  
  if (X == array2[mitad]):
    buscar = True
    
  elif (X < array2[mitad]):
    sup = mitad - 1
    
  else:
    inf = mitad + 1
    
if(buscar):
  print("el dato esta en el indice " + str(mitad + 1))
else:
  print ("el numero " + str(X) + " no se encuentra ")
