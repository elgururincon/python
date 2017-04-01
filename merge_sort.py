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
    middle = len(x)/2
    a = mergeSort(x[:middle])
    b = mergeSort(x[middle:])
    return merge(a,b)

array = []

import random
for i in range (10):
  array.append(random.randint(1 , 100))
  
print array

array2 = mergeSort(array)
print array2
