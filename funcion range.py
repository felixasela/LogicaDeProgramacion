# 1 Digitos del 0 al 9
for n in range(0, 10):
    print(n)

# 2 Números ente 100 y 199
for a in range(100, 200):
    print(a)

# 3 Números entre el 5 y el 20 saltando de 3 en 3
for b in range(5, 21, 3):
    print(b)

# 4 Números correlativos entre el ingresado por el usuario y uno menos del doble del mismo.
c = int(input("Digite un número: "))
for c in range(c, c*2):
    print(c)

# 5-6 Un listado de las vocales que aparecen en esa frase (sin repetirlas).
frase = input("Frase: ")
print("Vocales en la frase:")
for d in "aeiou":
  if d in frase:
    print(d)

# 7 Sumatoria de todos los números entre el 0 y el 100.
total = 0
for e in range(101):
    total = total + e
print("Sumatoria:", total)

# 8 años en el rango ingresado por el usuario, que sean bisiestos y múltiplos de 10.
añoInicio=int(input("Año inicial:"))
añoFin=int(input("Año final:"))
for año in range(añoInicio, añoFin+1):
   if not año%10==0:
       continue
   if not año%4==0:
       continue
   if año%100!=0 or año%400==0:
       print(año)

# 9 Factorial de un número
numero=int(input("Número:"))
f=1
if numero!=0:
    for i in range(1,numero+1):
        f=f*i
print("Factorial:", f)

# 10 primeros 10 números de la sucesión de Fibonacci.
n1=0
n2=1
print(n1)
print(n2)
for i in range(8):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3