def insertionSort(A):
   
  for j in range(1,len(A)):
    ins = A[j]

    i = j-1 
    
    while (i > -1) and ins < A[i]: 
   
      A[i+1]=A[i] 
      i=i-1 
      A[i+1] = ins
  
  return A
    

import random

array = []

for i in range (20):
  array.append(random.randint(1 , 100))
  
print array

array2 = insertionSort(array)
print array2
