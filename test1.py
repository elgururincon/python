minimo = abs(A[0] - A[1])

for i in range (n):
  
  for j in range (n):
    
    if i!=j:
      
      minimo = abs(A[i])-A[j]
      
      if abs(A[i])-A[j] < minimo:
        print (-1)
      else:
        minimo
      
  
print minimo
