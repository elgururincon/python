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

def insertionSort( array ):
    for i in range( len(array) ):
        x = array[i]
        index = i
        
        while(index > 0 and array[index - 1] > x):
            array[index] = array[index - 1]
            index -= 1
        
        array[index] = x
        
    return array
  
def merge(a,b):
  c = []
  while len(a) != 0 and len(b) != 0:
    if a[0] < b[0]:
      c.append(a[0])
      a.remove(a[0])
    else:
      c.append(b[0])
      b.remove(b[0])
    
  if len(a) == 0:
    c += b
  else:
    c += a
  return c

def mergeSort(x):

  if len(x) == 0 or len(x) == 1:
    return x
  else:
    mitad = len(x)/2
    a = mergeSort(x[:mitad])
    b = mergeSort(x[mitad:])
    return merge(a,b)

def quickSort(x):
    if len(x) == 1 or len(x) == 0:
      return x
    else:
      pivot = x[0]
      i = 0
      for j in range(len(x)-1):
        if x[j+1] < pivot:
          x[j+1],x[i+1] = x[i+1], x[j+1]
          i += 1
      
    x[0],x[i] = x[i],x[0]
    less = quickSort(x[:i])
    greater = quickSort(x[i+1:])
    less.append(x[i])
    return less + greater


import random
array = []

for i in range (10):
  array.append(random.randint(1 , 15))
  
print array

while True:
    print """

de que forma quiere ordenar?:
 
1 para BubbleSort
2 para InsertionSort
3 para MergeSort
4 para QuickSort

"""
    opcion=input(" ")

    if opcion == 1:
      array2 = bubbleSort(array)
      print ("escojio bubbleSort")
      print array2
      break
    elif opcion == 2:
      array2 = insertionSort(array)
      print ("escojio insertionSort")
      print array2
      break 
    elif opcion == 3:
      array2 = mergeSort(array)
      print ("escojio mergeSort")
      print array2
      break
    elif opcion == 4:
      array2 = quickSort(array)
      print ("escojio QuickSort")
      print array2
      break
    else:
        print "opcion incorrecta"
