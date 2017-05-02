array =[5,5,3,3,2,2,1]

n = len(array)
dif = 0
for i in range(n):
  
  for j in range(n):
    
    if i != j and array[i]== array[j]:
      break
    if (j==n):
      print array[i]

print array[i]
