# detector de palíndromos pero obviando espacios, puntos y carácteres acentuados.

fraseBase = input('Frase: ')

fraseBase = fraseBase.lower()

fraseProcesada = ''

for i in fraseBase:
    if i == ' ' or i == '.' or i == ',':
        pass
    elif i == 'á':
        fraseProcesada += 'a'
    elif i == 'é':
        fraseProcesada += 'e'
    elif i == 'í':
        fraseProcesada += 'i'
    elif i == 'ó':
        fraseProcesada += 'o'
    elif i == 'ú':
        fraseProcesada += 'u'
    elif i == 'ü':
        fraseProcesada += 'u'
    else:
        fraseProcesada += i

fraseInvert = ''

for i in fraseBase:
    if i == ' ' or i == '.' or i == ',':
        pass
    elif i == 'á':
        fraseInvert = 'a' + fraseInvert
    elif i == 'é':
        fraseInvert = 'e' + fraseInvert
    elif i == 'í':
        fraseInvert = 'i' + fraseInvert
    elif i == 'ó':
        fraseInvert = 'o' + fraseInvert
    elif i == 'ú':
        fraseInvert = 'u' + fraseInvert
    elif i == 'ü':
        fraseInvert = 'u' + fraseInvert
    else:
        fraseInvert = i + fraseInvert

if fraseProcesada == fraseInvert:
    print('La frase es palíndroma.')
else:
    print('La frase NO es palíndroma.')
