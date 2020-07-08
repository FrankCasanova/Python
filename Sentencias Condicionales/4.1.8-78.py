#programa que calcule el máximo de 5 números enteros.

a = int(input('Primer número: '))
b = int(input('Segúndo número: '))
c = int(input('Tercer número: '))
d = int(input('Cuarto número: '))
e = int(input('Quinto número: '))

candidato = a

if candidato < b:
    candidato = b
if candidato < c:
    candidato = c
if candidato < d:
    candidato = d
if candidato < e:
    candidato = e


print('El mayor es', candidato)                