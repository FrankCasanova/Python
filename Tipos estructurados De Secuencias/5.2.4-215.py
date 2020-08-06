#programa que almacene en a una lista list(range(1,4))y, a continuación, la modifique para que cada componente sea igual al cuadrado del componente original.

a = list(range(1,4))

a = [i*i for i in range(len(a))]
    
print(a)    

'''
este ejemplo muestra que podemos indicar
lo que queremos hacer antes de ejecutar el bucle for
antes de usar el tipico buble for
le da una elegancia exquisita.
'''



 

