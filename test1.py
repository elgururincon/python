array = []

for i in range (20):
  array.append(random.randint(1 , 20))

minimo = abs(array[0] - array[1])

for i in range (n):
  
  for j in range (n):
    
    if i!=j:
      
      minimo = abs(array[i])-array[j]
      
      if abs(array[i])-array[j] < minimo:
        print (-1)
      else:
        minimo
      
  
print minimo
