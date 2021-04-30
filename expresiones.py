i = 1
notas = 0
nota = True
while nota == True:
    notas = float(input("digite la nota #" + str(i) + ": "))
    i = i + 1
    if notas > 5:
        print("Las notas tienen que ser menores o iguales a 5")
    if i > 5:
        promedio = (notas * 0.15) + (notas * 0.2) + (notas * 0.15) + ((notas + i) * 0.3) + ((notas + i ) * 0.2) / 5
        print(promedio)
        break