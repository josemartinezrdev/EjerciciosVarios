from tabulate import tabulate
import os

msg = """

    a. Total de números ingresados
    b. Total de números pares ingresados
    c. Promedio de los números pares
    d. Promedio de los números impares
    e. Cuantos números son menores que 10
    f. Cuantos números están entre 20 y 50
    g. Cuantos números son mayores que 100
    h. Salir

"""

lstNumbers = []
lstPares = []
lstImpares = []
lstMenoresDiez = []
lstEntreVeinteCincuenta = []
lstEntreMayoresCien = []

isPositive = True
sumaPar = 0
sumaImpar = 0

def View(lstNumbers,lstPares,lstImpares,lstMenoresDiez,lstEntreVeinteCincuenta,lstEntreMayoresCien,isPositive):
    print(msg)
    op = input('-> ')
    if op.lower() == 'a':
        print(f'El total de números fue: {len(lstNumbers)}')
        View(lstNumbers,lstPares,lstImpares,lstMenoresDiez,lstEntreVeinteCincuenta,lstEntreMayoresCien,isPositive)
    elif op.lower() == 'b':
        print(f'El total de números pares fue: {len(lstPares)}')
        View(lstNumbers,lstPares,lstImpares,lstMenoresDiez,lstEntreVeinteCincuenta,lstEntreMayoresCien,isPositive)
    elif op.lower() == 'c':
        print(f'El promedio de números pares es: {promedioPar}')
        View(lstNumbers,lstPares,lstImpares,lstMenoresDiez,lstEntreVeinteCincuenta,lstEntreMayoresCien,isPositive)
    elif op.lower() == 'd':
        print(f'El promedio de números impares es: {promedioImpar}')
        View(lstNumbers,lstPares,lstImpares,lstMenoresDiez,lstEntreVeinteCincuenta,lstEntreMayoresCien,isPositive)
    elif op.lower() == 'e':
        print(f'La cantidad de números menores de 10 es: {len(lstMenoresDiez)}')
        View(lstNumbers,lstPares,lstImpares,lstMenoresDiez,lstEntreVeinteCincuenta,lstEntreMayoresCien,isPositive)
    elif op.lower() == 'f':
        print(f'La cantidad de números mayores de 20 pero menores que 50 es: {len(lstEntreVeinteCincuenta)}')
        View(lstNumbers,lstPares,lstImpares,lstMenoresDiez,lstEntreVeinteCincuenta,lstEntreMayoresCien,isPositive)
    elif op.lower() == 'g':
        print(f'La cantidad de números mayores de 100 es: {len(lstEntreMayoresCien)}')
        View(lstNumbers,lstPares,lstImpares,lstMenoresDiez,lstEntreVeinteCincuenta,lstEntreMayoresCien,isPositive)
    elif op.lower() == 'h':
        isPositive = False
    else:
        print('La opción no es valida')
        View(lstNumbers,lstPares,lstImpares,lstMenoresDiez,lstEntreVeinteCincuenta,lstEntreMayoresCien,isPositive)

while isPositive:
    os.system('cls')
    num = int(input('Ingrese un numero entero positivo:\n-> '))
    if num > 0:
        lstNumbers.append(num)
        if num % 2 == 0:
            lstPares.append(num)
            sumaPar += num
            promedioPar = sumaPar / len(lstPares)
        else:
            lstImpares.append(num)
            sumaImpar += num
            promedioImpar = sumaImpar / len(lstImpares)
        if num < 10:
            lstMenoresDiez.append(num)
        elif (num >= 20) and (num <= 50):
            lstEntreVeinteCincuenta.append(num)
        elif (num > 100):
            lstEntreMayoresCien.append(num)

    else:
        View(lstNumbers,lstPares,lstImpares,lstMenoresDiez,lstEntreVeinteCincuenta,lstEntreMayoresCien,isPositive)
