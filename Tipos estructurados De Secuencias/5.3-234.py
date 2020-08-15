# disponemos de una cadena que contiene una frase cuyas palabras están separadas
# por un número arbitriario de espacioes en blanco. podrías <<estandarizar>> la separación de palabras en una sola línea python?
# por estandarizar queremos decir que la cadena no empiece ni acabe con espacioes en blanco y que cada palabra se separe de la
# siguiente por un único espacio en blanco

frase = ' hola      estamos   en una cosita   que no se    sabe  cual es    '

frase = frase.split()
frase = ' '.join(frase) 

print(frase)