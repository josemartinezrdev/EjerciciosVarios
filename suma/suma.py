import os

def suma():

    try:
        num1 = int(input('Ingrese número 1: \n-> '))
        if num1 > 0:
            num2 = int(input('Ingrese número 2: \n-> '))
            if num2 > 0:
                num3 = int(input('Ingrese número 3: \n-> '))
                if num3 > 0:
                    print(f'La suma de los números es: {num1 + num2 + num3}')
        else:
            print('Los números deben ser enteros positivos')
            os.system('pause')
            suma()
    except ValueError:
        print('El numero ingresado no es valido')
        os.system('pause')
        suma()
    else:
        pass

suma()