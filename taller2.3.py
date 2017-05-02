import random
array = []

for i in range (5):
  array.append(random.randint(1 , 15))


n = len(array)
d = input("numero a comparar")
valor = 0

for i in range (n):
  
  for j in range (i+1):
    
    if i!=j:
      
      diferencia = abs(array[i]-array[j])
      
      if abs(array[i] - array[j]) == d:
        valor = valor +1

print valor 

print array

