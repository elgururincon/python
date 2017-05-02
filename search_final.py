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

def binarySearch(array2):

  n= len(array2)
  inf = 0
  sup = n-1
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
    


def interpolationSearch(array2):

  n = len(array2)
  inf =  0 
  sup = n-1
  buscar = False
  
  x = int(input("ingresa numero"))

  while ( not(buscar) and inf <= sup):
    
    mitad = (inf +(array2[sup] - array2[inf]) * (x - array2[inf]))
    
    if (x == array2[mitad]):
      buscar = True
    
    elif (x < array2[mitad]):
      sup = mitad - 1
    
    else:
      inf = mitad + 1
    
  if(buscar):
    print("el dato esta en el indice " + str(mitad + 1))
  else:
    print ("el numero " + str(x) + " no se encuentra ")
    

while True:
    print """
de que forma quiere buscar?:
 
1 para Binary Search
2 para Interpolation Search

"""
    opcion=input(" ")

    if opcion == 1:
      binarySearch(array2)
      print ("escojio Binary Search")
      break
    
    elif opcion == 2:
      interpolationSearch(array2)
      print ("escojio Interpolation Search")
      break 
