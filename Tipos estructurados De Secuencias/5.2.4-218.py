#mirar en el libro.

a = list(range(0,5))
b = list(range(0,5))
c = a
d = b[:]
e = a+b
f = b[:1]
g = b[0]
c[0] = 100
d[0] = 200
c[0] = 300

print(a,b,c,d,e,f,g)