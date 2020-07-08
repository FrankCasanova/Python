# 5 PALABRA MÁS CORTA Y NO SE ACEPTA QUE LAS MAYUSCULAS SEAN MENORES.

word1 = input('Palabra 1: ')
word2 = input('Palabra 2: ')
word3 = input('Palabra 3: ')
word4 = input('Palabra 4: ')
word5 = input('Palabra 5: ')

candidato = word1.lower()

if word2.lower() < candidato:
    candidato = word2.lower()
if word3.lower() < candidato:
    candidato = word3.lower()
if word4.lower() < candidato:
    candidato = word4.lower()
if word5.lower() < candidato:
    candidato = word5.lower()
    
print('La palabra más corta es', candidato)