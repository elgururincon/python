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

for i in range (20):
  array.append(random.randint(1 , 100))
  
print array

array2 = bubbleSort(array)
print array2
