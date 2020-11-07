#programa que muestra la rentabilidad de un dinero invertido.

#datos

euros = float(input('Cantidad de euros: '))
tax = float(input('Tasa de interes: '))
años = float(input('Cantidad de añoos: '))

#fórmula

rentabilidad = euros * (1+(tax/100))**años

print('La rentabilidad para un capital de {0} con un interes de {1} por ciento a {2} años, es de: {3} euros'.format(euros, tax, años, rentabilidad))
