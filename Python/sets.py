from cubo import *

#declaração
s = set()

#adicionando elementos
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(5)

s.remove(1)

for i in s:
    print(f"O quadrado de {i} é {quadrado(i)}")

for i in s:
    print(f"O cubo de {i} é {cube(i)}")
    
print(s)
print(f"O set possui {len(s)} elementos")