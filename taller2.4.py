array =[2, 230, 11, 9, 7, 28, 22, 15, 5, 19, 36,  17]


n = len(array)
maximo = abs(array[0] - array[1])

for i in range (n):
  
  for j in range (n):
    
    if i<j:
      
      maximo = abs(array[i]-array[j]) if abs(array[i] - array[j]) > maximo else maximo
 

print array  
print maximo
